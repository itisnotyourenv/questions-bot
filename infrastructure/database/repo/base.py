from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete


class BaseRepo:
    """
    A class representing a base repository for handling database operations.

    Attributes:
        session (AsyncSession): The database session used by the repository.

    """
    model = None

    def __init__(self, session):
        self.session: AsyncSession = session
        if self.model is None:
            raise ValueError("Model is not set.")

    async def get_or_none(self, item_pk: int | str) -> Optional[model]:
        """
        Returns a class object if it exists in the database.

        :param item_pk: The item's ID.
        :return: Class object, None if it doesn't exist.
        """
        return await self.session.get(self.model, item_pk)

    async def create(self, **kwargs) -> model:
        """
        Creates a class object in the database.

        :param kwargs: The class object's attributes.
        :return: The created class object.
        """
        item = self.model(**kwargs)
        self.session.add(item)
        await self.session.commit()
        return item

    async def get_by_filter(self, **kwargs) -> model:
        """
        Returns a class object if it exists in the database.

        :param kwargs: The item's ID.
        :return: Class object, None if it doesn't exist.
        """
        item = await self.session.execute(select(self.model).filter_by(**kwargs))
        return item.scalars().first()

    async def delete(self, **kwargs) -> None:
        """
        Deletes a class object in the database.

        :param kwargs: The class object's attributes.
        :return: The deleted class object.
        """
        item = delete(self.model).filter_by(**kwargs)
        await self.session.execute(item)
        await self.session.commit()
