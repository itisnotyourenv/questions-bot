from dataclasses import dataclass


@dataclass
class QuestionStates:
    WAIT_FOR_QUESTION_STATE = "wfq"
    USER_ID_PARAM: str = "user_id"


@dataclass
class AnswerStates:
    WAIT_FOR_ANSWER_STATE = "wfa"
    USER_ID_PARAM: str = "user_id"
