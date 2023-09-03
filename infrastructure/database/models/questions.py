from sqlalchemy import String
from sqlalchemy import BIGINT, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class Question(Base, TimestampMixin, TableNameMixin):
    question_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    question_from: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.user_id", ondelete="NO ACTION"))
    question_to: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.user_id", ondelete="NO ACTION"))
    text = mapped_column(String(4096))

    def __repr__(self):
        return f"<User {self.question_from} {self.question_to}>"
