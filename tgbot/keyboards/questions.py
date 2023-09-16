from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.misc.callback_data import AnswerCallbackData


def question_answer_markup(question_id: int, author_id: int):
    """
    The function returns the keyboard with the buttons "Generate image" and "Block author".

    :param question_id: ID of the question to be answered.
    :param author_id: ID of the user who is the author of the question.
    :return: InlineKeyboardMarkup
    """
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Сгенерировать изображение",
                    callback_data=AnswerCallbackData.generate_image_callback(question_id),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Заблокировать автора",
                    callback_data=AnswerCallbackData.block_author_callback(author_id),
                )
            ],
        ]
    )
    return markup


def unblock_author_markup(author_id: int):
    """
    The function returns the keyboard with the buttons "Generate image" and "Block author".

    :param author_id: ID of the user who is the author of the question.
    :return: InlineKeyboardMarkup
    """
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Разблокировать автора",
                    callback_data=AnswerCallbackData.unblock_author_callback(author_id),
                )
            ],
        ]
    )
    return markup
