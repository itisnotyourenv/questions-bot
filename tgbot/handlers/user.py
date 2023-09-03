from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.misc.states import QuestionStates

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, command: CommandObject, repo: RequestsRepo, state: FSMContext):
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
    # example: t.me/q_bot?start=244472550
    # validate that the argument is a number and not the same as the current user
    if command.args and command.args.isdigit() and int(command.args) != message.from_user.id:
        # 1) Check that the user from deeplink exists
        q_user = await repo.users.get_or_none(int(command.args))
        if not q_user:
            # todo -add greeting message
            await message.reply("Пользователь не найден")
            return

        text = (
            "<b>Введите ваш вопрос</b>\n\n"
            "Вы также можете использовать фотографию или видео чтобы уточнить вопрос.\n"
        )
        await message.answer(text)

        await state.set_data({QuestionStates.USER_ID_PARAM: command.args})
        await state.set_state(QuestionStates.WAIT_FOR_QUESTION_STATE)
        return

    greeting_message = (
        "<b>Твоя ссылка для вопросов</b>:\n"
        f"t.me/stagging_bot?start={message.from_user.id}\n\n"
        "Поделись ей со своими друзьями и подписчиками, чтобы они могли задать тебе вопрос!."
    )

    await message.answer(greeting_message)
    # todo - user method copy_to when we would send message to address
