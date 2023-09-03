from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import Question
from infrastructure.database.repo.base import BaseRepo


class QuestionsService(BaseRepo):
    pass