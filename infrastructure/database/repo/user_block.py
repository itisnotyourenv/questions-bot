from infrastructure.database.models import UserBlocked
from infrastructure.database.repo.base import BaseRepo


class UserBlockRepo(BaseRepo):
    model = UserBlocked
