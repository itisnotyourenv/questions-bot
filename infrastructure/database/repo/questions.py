from infrastructure.database.models import Question
from infrastructure.database.repo.base import BaseRepo

from sqlalchemy import select, func


class QuestionsService(BaseRepo):
    model = Question

    async def count(self):
        """
        Returns the number of users in the database.
        :return: The number of users in the database.
        """
        return await self.session.scalar(select(func.count(self.model.question_id)))
