import logging

from aiogram import Router
from aiogram.filters import CommandStart, CommandObject, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.keyboards.questions import unblock_author_markup
from tgbot.misc.states import QuestionStates
from tgbot.misc.callback_data import AnswerCallbackData
from tgbot.config import load_config
from tgbot.services.questions import block_user

user_router = Router()
config = load_config()


@user_router.message(CommandStart())
async def user_start(
        message: Message, command: CommandObject, repo: RequestsRepo, state: FSMContext,
):
    """
    Handle the '/start' command and process deep link parameters if provided.

    :param: message: The incoming message object from the user.
    :param: command: The command object representing the '/start' command with arguments.
    :param: repo: The RequestsRepo object for managing database requests.
    :param: state: The FSMContext object for managing conversation state.
    :return: None

    Notes:
        - If deep link parameters are provided, this function processes the information, performs necessary actions,
          and guides the user to input a question while maintaining the state.
        - If no deep link parameters are provided, a simple welcome message is sent to the user.
    """
    # validate that the argument is a number and not the same as the current user
    if command.args and command.args.isdigit() and int(command.args) != message.from_user.id:
        # 1) Check that the user from deeplink exists
        q_user = await repo.users.get_or_none(int(command.args))
        if not q_user:
            await message.reply("Пользователь не найден")
            return

        user_is_blocked = await repo.user_block.get_by_filter(
            user_id=int(command.args), blocked_user_id=message.from_user.id
        )
        if user_is_blocked:
            await message.reply("Вы заблокированы пользователем")
            return

        text = (
            "<b>Введите ваш вопрос</b>\n\n"
            "Вы также можете использовать фотографию или видео чтобы уточнить вопрос.\n\n\n"
            "<a href='https://github.com/itisnotyourenv/questions-bot'>GitHub проекта</a>"
        )
        await message.answer(text)

        await state.set_data({QuestionStates.USER_ID_PARAM: command.args})
        await state.set_state(QuestionStates.WAIT_FOR_QUESTION_STATE)
        return

    greeting_message = (
        "<b>Твоя ссылка для вопросов</b>:\n"
        f"{config.tg_bot.bot_url}?start={message.from_user.id}\n\n"
        "Поделись ей со своими друзьями и подписчиками, чтобы они могли задать тебе вопрос!"
    )

    await message.answer(greeting_message)


@user_router.callback_query(Text(startswith=AnswerCallbackData.block_author))
async def clb_block_author_handler(call: CallbackQuery, repo: RequestsRepo):
    """
    Handle the user's request to block the author of the question.

    :param: message: The incoming message object from the user.
    :param: repo: The RequestsRepo object for managing database requests.
    :return: None

    Notes:
        - This function blocks the author of the question.
    """
    logging.info("User %s sent block author request", call.from_user.id)

    # get message ID from callback data
    message_id = int(call.data.split("=")[1])
    user_block_id = await block_user(call.from_user.id, message_id, repo)
    markup = unblock_author_markup(user_block_id)
    await call.message.edit_text(text=call.message.text, reply_markup=markup)


@user_router.callback_query(Text(startswith=AnswerCallbackData.unblock_author))
async def clb_unblock_author_handler(call: CallbackQuery, repo: RequestsRepo):
    """
    Handle the user's request to block the author of the question.

    :param: message: The incoming message object from the user.
    :param: repo: The RequestsRepo object for managing database requests.
    :return: None

    Notes:
        - This function blocks the author of the question.
    """
    logging.info("User %s sent unblock author request", call.from_user.id)

    message_id = call.data.split("=")[1]
    await repo.user_block.delete(user_blocked_id=int(message_id))
    await call.message.edit_text(text=call.message.text, reply_markup=None)
    await call.answer("Пользователь разблокирован", show_alert=True)
