import logging
from time import sleep

from aiogram import Router, Bot
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.keyboards.questions import question_answer_markup
from tgbot.misc.states import QuestionStates, AnswerStates
from tgbot.misc.callback_data import AnswerCallbackData
from tasks.tasks import generate_image

answer_router = Router()


@answer_router.callback_query(Text(startswith=AnswerCallbackData.answer_to_question))
async def answer_callback_handler(call, repo: RequestsRepo, bot: Bot, state: FSMContext):
    question_id = call.data.split("=")[1]
    question = await repo.questions.get_or_none(int(question_id))
    await bot.send_message(question.question_from, call.message.text)


    # todo - добавить кнопку для отмены ответа
    await call.message.answer("Введите ответное сообщение")

    await state.set_data({AnswerStates.USER_ID_PARAM: question.question_from})
    await state.set_state(AnswerStates.WAIT_FOR_ANSWER_STATE)


@answer_router.message(StateFilter(AnswerStates.WAIT_FOR_ANSWER_STATE))
async def question_handler(message: Message, state: FSMContext, repo: RequestsRepo):
    logging.info("User %s sent answer", message.from_user.id)
    generate_image.delay(message.from_user.id, message.text)

    state_data = await state.get_data()
    user_id = state_data.get(QuestionStates.USER_ID_PARAM)

    await repo.questions.create(
        question_id=message.message_id,
        question_from=message.from_user.id,
        question_to=int(user_id),
        text=message.text,
    )

    markup = question_answer_markup(message.message_id)
    await message.send_copy(user_id, reply_markup=markup)

    await message.answer("Ваш вопрос отправлен адресату")
    await state.clear()
