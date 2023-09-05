import logging

from aiogram import Bot
from aiogram.types import FSInputFile

from image_generator.builder import generate_image
from tgbot.config import load_config

config = load_config()

bot = Bot(token=config.tg_bot.token)


async def start_image_generation(ctx: dict, user_id: int, text: str):
    print(f"user={user_id}")
    print(f"text={text}")
    logging.info("Start image generation for user %s", user_id)
    path = generate_image(text)
    print(path)
    photo = FSInputFile(path)

    await bot.send_photo(user_id, photo)

