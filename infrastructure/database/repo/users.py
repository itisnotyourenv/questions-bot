from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import func

from infrastructure.database.models import User
from infrastructure.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    model = User

    async def get_or_create_user(
        self,
        user_id: int,
        full_name: str,
        language: str,
        username: Optional[str] = None,
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param user_id: The user's ID.
        :param full_name: The user's full name.
        :param language: The user's language.
        :param username: The user's username. It's an optional parameter.
        :return: User object, None if there was an error while making a transaction.
        """

        insert_stmt = select(User).from_statement(
            insert(User)
            .values(
                user_id=user_id,
                username=username,
                full_name=full_name,
                language=language,
            )
            .returning(User)
            .on_conflict_do_update(
                index_elements=[User.user_id],
                set_=dict(
                    username=username,
                    full_name=full_name,
                ),
            )
        )
        result = await self.session.scalars(insert_stmt)

        await self.session.commit()
        return result.first()

    async def count(self):
        """
        Returns the number of users in the database.
        :return: The number of users in the database.
        """
        return await self.session.scalar(select(func.count(self.model.user_id)))
