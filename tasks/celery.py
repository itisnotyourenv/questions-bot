from celery import Celery

from tgbot.config import load_config

config = load_config()


celery_app = Celery('tasks', broker=config.redis.dsn(), include=['tasks.tasks'])
