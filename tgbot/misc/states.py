from dataclasses import dataclass


@dataclass
class QuestionDataClass:
    WAIT_FOR_QUESTION_STATE = "wfq"
    USER_ID_PARAM: str = "user_id"
