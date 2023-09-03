import logging

from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.keyboards.questions import question_answer_markup
from tgbot.misc.states import QuestionDataClass

question_router = Router()


@question_router.message(StateFilter(QuestionDataClass.WAIT_FOR_QUESTION_STATE))
async def question_handler(message: Message, state: FSMContext, repo: RequestsRepo):
    """
    Handle the user's question and send it to the recipient.
    """
    logging.info("User %s sent question", message.from_user.id)

    state_data = await state.get_data()
    user_id = state_data.get(QuestionDataClass.USER_ID_PARAM)
    markup = question_answer_markup(message.message_id)
    await message.send_copy(user_id, reply_markup=markup)
    await message.answer("Ваш вопрос отправлен адресату")
