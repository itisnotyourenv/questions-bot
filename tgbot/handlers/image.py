import logging

from aiogram import Router, Bot
from aiogram.filters import Text
from aiogram import types
from arq.connections import ArqRedis, create_pool

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.misc.callback_data import AnswerCallbackData

image_router = Router()


@image_router.callback_query(Text(startswith=AnswerCallbackData.generate_image))
async def image_generation_handler(call: types.CallbackQuery, repo: RequestsRepo, bot: Bot, config):
    logging.info("User %s sent answer", call.from_user.id)
    question_id = call.data.split("=")[1]

    question = await repo.questions.get_or_none(int(question_id))
    redis: ArqRedis = await create_pool(settings_=config.misc.arq_redis_settings)
    await redis.enqueue_job(
        "start_image_generation",
        call.from_user.id,
        question.text,
    )

    await bot.send_chat_action(call.from_user.id, "upload_photo")
    await call.answer("tamam")
