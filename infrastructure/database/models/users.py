from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT, Boolean, true, ForeignKey, INT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class User(Base, TimestampMixin, TableNameMixin):
    """
    This class represents a User in the application.
    If you want to learn more about SQLAlchemy and Alembic, you can check out the following link to my course:
    https://www.udemy.com/course/sqlalchemy-alembic-bootcamp/?referralCode=E9099C5B5109EB747126

    Attributes:
        user_id (Mapped[int]): The unique identifier of the user.
        username (Mapped[Optional[str]]): The username of the user.
        full_name (Mapped[str]): The full name of the user.
        active (Mapped[bool]): Indicates whether the user is active or not.
        language (Mapped[str]): The language preference of the user.

    Methods:
        __repr__(): Returns a string representation of the User object.

    Inherited Attributes:
        Inherits from Base, TimestampMixin, and TableNameMixin classes, which provide additional attributes and functionality.

    Inherited Methods:
        Inherits methods from Base, TimestampMixin, and TableNameMixin classes, which provide additional functionality.

    """
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    username: Mapped[Optional[str]] = mapped_column(String(128))
    full_name: Mapped[str] = mapped_column(String(128))
    active: Mapped[bool] = mapped_column(Boolean, server_default=true())
    language: Mapped[str] = mapped_column(String(10), server_default=text("'en'"))
    # we will add here info about a user that invited this user for a question
    referrer_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.user_id", ondelete="SET NULL"), nullable=True)

    # todo - learn about relationships
    # referrer = relationship("User")

    def __repr__(self):
        return f"<User {self.user_id} {self.username} {self.full_name}>"


class UserBlocked(Base, TimestampMixin):
    """
    This class represents a UserBlocked in the application.
    """
    __tablename__ = "users_blocked"

    user_blocked_id: Mapped[int] = mapped_column(INT, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.user_id", ondelete="CASCADE"))
    blocked_user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.user_id", ondelete="CASCADE"))

    def __repr__(self):
        return f"<UserBlocked {self.user_id} {self.blocked_user_id}>"
