from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.misc.states import QuestionDataClass

question_router = Router()


@question_router.message(StateFilter(QuestionDataClass.WAIT_FOR_QUESTION_STATE))
async def question_handler(message: Message, state: FSMContext, repo: RequestsRepo):
    state_data = await state.get_data()
    user_id = state_data.get(QuestionDataClass.USER_ID_PARAM)
    await message.send_copy(user_id)
    await message.answer("Ваш вопрос отправлен адресату")
