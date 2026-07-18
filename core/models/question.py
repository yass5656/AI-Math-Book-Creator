from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


class QuestionType(str, Enum):
    MULTIPLE_CHOICE = "Multiple Choice"
    SHORT_ANSWER = "Short Answer"
    FILL_IN_THE_BLANK = "Fill in the Blank"
    MATCHING = "Matching"
    TRUE_FALSE = "True / False"
    WORD_PROBLEM = "Word Problem"


class Question(BaseModel):

    question_id: str

    curriculum: str

    stage: str

    term: int

    unit: str

    learning_object: str

    skill: str

    pattern_id: str

    difficulty: Difficulty

    question_type: QuestionType

    marks: int = 1

    estimated_time: int = Field(
        default=1,
        description="Minutes"
    )

    question_text: str

    answer: str

    hint: Optional[str] = None

    common_mistake: Optional[str] = None

    worked_solution: Optional[str] = None

    progression_style: bool = False

    workbook_style: bool = False

    book_style: bool = False
