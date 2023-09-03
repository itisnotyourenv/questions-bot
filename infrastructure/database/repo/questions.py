from infrastructure.database.models import Question
from infrastructure.database.repo.base import BaseRepo


class QuestionsService(BaseRepo):
    model = Question
