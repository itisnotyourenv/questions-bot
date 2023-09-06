import logging

from aiogram import types, Router

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.services.questions import send_question

reply_router = Router()


@reply_router.message()
async def bot_echo(message: types.Message, repo: RequestsRepo, ):
    logging.info("User %s sent message %s", message.from_user.id, message.text)
    if message.reply_to_message:

        message_id = message.reply_to_message.message_id
        question = await repo.questions.get_by_filter(to_message_id=message_id)
        await send_question(message, repo, question.question_from, reply_to_message_id=question.from_message_id)
    else:
        await message.answer("Неверный формат сообщения.")
