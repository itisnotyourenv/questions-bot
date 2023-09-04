from dataclasses import dataclass


@dataclass(frozen=True)
class AnswerCallbackData:
    answer_to_question: str = "atq"
    generate_image: str = "gi"

    @classmethod
    def answer_callback(cls, question_id: int):
        return f"{cls.answer_to_question}={question_id}"

    @classmethod
    def generate_image_callback(cls, question_id: int):
        return f"{cls.generate_image}={question_id}"
