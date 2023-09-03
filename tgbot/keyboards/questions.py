from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.misc.callback_data import AnswerCallbackData


def question_answer_markup(question_id: int):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Ответить",
                    callback_data=AnswerCallbackData.answer_callback(question_id),
                )
            ]
        ]
    )
    return markup
