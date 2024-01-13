from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from infrastructure.database.repo.requests import RequestsRepo

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(Command("stats"))
async def admin_start(message: Message, repo: RequestsRepo):
    users_count = await repo.users.count()
    questions_count = await repo.questions.count()

    text = (
        "📊 Небольшая статистика:\n\n"
        f"👤 Пользователей: {users_count}\n"
        f"❓ Вопросов: {questions_count}\n"
    )
    await message.answer(text)
