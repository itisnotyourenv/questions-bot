import logging

from aiogram import Bot
from aiogram.types import FSInputFile
from aiogram.exceptions import TelegramBadRequest

from image_generator.builder import generate_image
from tgbot.config import load_config

config = load_config()

bot = Bot(token=config.tg_bot.token)


async def start_image_generation(ctx: dict, user_id: int, text: str):
    """
    Generate image and send it to user

    :param ctx: Context from arq.
    :param user_id: User id to send image.
    :param text: Text to generate image.
    :return: None
    """
    logging.info("Start image generation for user %s", user_id)
    try:
        path = generate_image(text)
        await send_image(user_id, path, caption=text)
    except FileNotFoundError:
        logging.exception("Error while generating image for user %s", user_id)
        return
    logging.info("Generated image for user %s saved to %s", user_id, path)


async def send_image(user_id: int, image_path: str, caption: str = None):
    """
    Send image to user

    :param user_id: User id to send image.
    :param caption: Caption for image.
    :param image_path: Path to image.
    :return: None
    """
    logging.info("Sending image to user %s", user_id)
    photo = FSInputFile(image_path)
    try:
        await bot.send_photo(user_id, photo, caption=caption)
    except TelegramBadRequest:
        logging.exception("Error while sending image to user %s", user_id)
