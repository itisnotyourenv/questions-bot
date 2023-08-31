from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio.session import AsyncSession

from tgbot.filters.admin import AdminFilter
from infrastructure.database.models import User
from infrastructure.database.repo.requests import RequestsRepo

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message, session: AsyncSession, user: User, repo: RequestsRepo):
    await message.answer("tamam")
