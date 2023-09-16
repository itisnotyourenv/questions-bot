from dataclasses import dataclass


@dataclass(frozen=True)
class AnswerCallbackData:
    answer_to_question: str = "atq"
    generate_image: str = "gi"
    block_author: str = "ba"
    unblock_author: str = "uba"

    @classmethod
    def answer_callback(cls, question_id: int):
        return f"{cls.answer_to_question}={question_id}"

    @classmethod
    def generate_image_callback(cls, question_id: int):
        return f"{cls.generate_image}={question_id}"

    @classmethod
    def block_author_callback(cls, author_id: int):
        return f"{cls.block_author}={author_id}"

    @classmethod
    def unblock_author_callback(cls, author_id: int):
        return f"{cls.unblock_author}={author_id}"
