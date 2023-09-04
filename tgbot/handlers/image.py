import logging

from aiogram import Router, Bot
from aiogram.filters import Text
from aiogram import types

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.misc.callback_data import AnswerCallbackData
from tasks.tasks import generate_image

image_router = Router()


@image_router.callback_query(Text(startswith=AnswerCallbackData.generate_image))
async def image_generation_handler(call: types.CallbackQuery, repo: RequestsRepo, bot: Bot):
    logging.info("User %s sent answer", call.from_user.id)
    question_id = call.data.split("=")[1]

    question = await repo.questions.get_or_none(int(question_id))
    print(question.text)
    print()
    print()
    print()
    generate_image.delay(call.from_user.id, question.text)

    await bot.send_chat_action(call.from_user.id, "upload_photo")
