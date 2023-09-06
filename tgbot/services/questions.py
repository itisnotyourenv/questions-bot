from aiogram import types
from aiogram.exceptions import TelegramBadRequest

from infrastructure.database.repo.requests import RequestsRepo


async def send_question(
        message: types.Message,
        repo: RequestsRepo,
        chat_id: int,
        reply_to_message_id: int = None,
):
    message.__config__.allow_mutation = True
    question_text_pattern = "<b>{prefix}</b>\n\n{question}\n\n↩️ <i>Свайпни для ответа.</i>"

    if reply_to_message_id is not None:
        prefix = "Ответ на ваше сообщение:"
    else:
        prefix = "Анонимный вопрос:"

    if message.text:
        message.text = question_text_pattern.format(prefix=prefix, question=message.text)
    elif message.caption:
        message.caption = question_text_pattern.format(prefix=prefix, question=message.caption)

    try:
        result = await message.send_copy(chat_id, reply_to_message_id=reply_to_message_id)
        await repo.questions.create(
            question_id=message.message_id,
            question_from=message.from_user.id,
            from_message_id=message.message_id,
            question_to=int(chat_id),
            to_message_id=result.message_id,
            text=message.text,
        )
        await message.answer("Сообщение отправлено.")
    except TelegramBadRequest:
        await message.answer("Пользователь по каким-то причинам не может получать сообщения от бота.")
