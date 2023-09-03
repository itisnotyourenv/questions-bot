from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def question_answer_markup(question_id: int):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Ответить",
                    callback_data=f"answer:{question_id}"
                )
            ]
        ]
    )
    return markup
