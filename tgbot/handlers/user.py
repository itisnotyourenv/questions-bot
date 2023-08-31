from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from infrastructure.database.repo.requests import RequestsRepo

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, session):
    print(session)
    print(type(session))
    await message.reply("Вітаю, звичайний користувач!")
