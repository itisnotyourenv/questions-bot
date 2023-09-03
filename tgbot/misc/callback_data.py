from dataclasses import dataclass


@dataclass(frozen=True)
class AnswerCallbackData:
    answer_to_question: str = "atq"

    @classmethod
    def answer_callback(cls, question_id: int):
        return f"{cls.answer_to_question}={question_id}"
