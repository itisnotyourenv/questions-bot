import logging

from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode

from infrastructure.database.repo.requests import RequestsRepo

echo_router = Router()


@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message, repo: RequestsRepo):
    logging.info("User %s sent message %s", message.from_user.id, message.text)
    text = ["Ntst", message.text]
    if message.reply_to_message:
        print()
        print()
        print()
        print()
        message_id = message.reply_to_message.message_id
        print(f"message_id={message_id}")
        question = await repo.questions.get_by_filter(message_id=message_id)
        print(question)
        print()
        print()
        print()
        print()

    await message.answer("\n".join(text))


@echo_router.message(F.text)
async def bot_echo_all(message: types.Message, state: FSMContext):
    logging.info("User %s sent message %s", message.from_user.id, message.text)
    state_name = await state.get_state()
    text = [
        f"Эхо с состояние {hcode(state_name)}",
        "Текст:",
        hcode(message.text),
    ]
    await message.answer("\n".join(text))
