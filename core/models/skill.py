from typing import List
from pydantic import BaseModel, Field


class Skill(BaseModel):

    id: str

    title: str

    learning_objective: str

    difficulty: List[str] = Field(default_factory=list)

    question_types: List[str] = Field(default_factory=list)

    generator: str

    patterns: List[str] = Field(default_factory=list)

    cambridge_tags: List[str] = Field(default_factory=list)

    progression_test: bool = False

    workbook: bool = False

    practice_book: bool = False