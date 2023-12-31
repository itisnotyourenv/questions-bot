import logging

from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode

echo_router = Router()


@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message):
    logging.info("User %s sent message %s", message.from_user.id, message.text)
    await message.answer("Эхо без состояния")


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


@echo_router.callback_query(F.data)
async def bot_echo_all(call: types.CallbackQuery, state: FSMContext):
    logging.info("User %s sent message %s", call.from_user.id, call.data)
    state_name = await state.get_state()
    text = [
        f"Эхо с состояние {hcode(state_name)}",
        "callback_data:",
        hcode(call.data),
    ]
    await call.answer("\n".join(text), show_alert=True)
