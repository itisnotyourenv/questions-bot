import asyncio

from tgbot.config import load_config
from tgbot.tasks.image_generation import start_image_generation

config = load_config()


async def startup(ctx):
    """
    Binds a connection set to the db object.
    """
    print('startup')


async def shutdown(ctx):
    """
    Pops the bind on the db object.
    """
    print('shutdown')


# WorkerSettings defines the settings to use when creating the work,
# it's used by the arq cli.
# For a list of available settings, see https://arq-docs.helpmanual.io/#arq.worker.Worker
class WorkerSettings:
    functions = [start_image_generation]
    on_startup = startup
    on_shutdown = shutdown
    redis_settings = config.misc.arq_redis_settings
