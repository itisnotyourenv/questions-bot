from aiogram import types
from aiogram.exceptions import TelegramBadRequest

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.keyboards.questions import question_answer_markup


async def send_question(
        message: types.Message,
        repo: RequestsRepo,
        chat_id: int,
        reply_to_message_id: int = None,
):
    original_text = message.text  # cache original text, we use it later to save in db
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
        markup = question_answer_markup(message.message_id)
        result = await message.send_copy(chat_id, reply_to_message_id=reply_to_message_id, reply_markup=markup)
        await repo.questions.create(
            question_id=message.message_id,
            question_from=message.from_user.id,
            from_message_id=message.message_id,
            question_to=int(chat_id),
            to_message_id=result.message_id,
            text=original_text,
        )
        await message.answer("Сообщение отправлено.")
    except TelegramBadRequest:
        await message.answer("Пользователь по каким-то причинам не может получать сообщения от бота.")


async def block_user(
        user_id: int,
        question_id: int,
        repo: RequestsRepo,
) -> int:
    """
    Block user by message id

    :param user_id: ID of the user that wants to block the author
    :param question_id: ID of the message that user sent
    :param repo: RequestsRepo instance
    :return: ID of the user_block record
    """
    question = await repo.questions.get_by_filter(question_id=question_id)
    user_block = await repo.user_block.create(user_id=user_id, blocked_user_id=question.question_from)
    return user_block.user_blocked_id
