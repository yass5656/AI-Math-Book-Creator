from pydantic import BaseModel, Field
from typing import List


class QuestionBlock(BaseModel):
    title: str
    style: str
    count: int
    difficulty: str


class Page(BaseModel):
    page_number: int
    title: str
    blocks: List[QuestionBlock] = Field(default_factory=list)


class Lesson(BaseModel):
    lesson_name: str
    pages: List[Page] = Field(default_factory=list)


class Unit(BaseModel):
    unit_name: str
    lessons: List[Lesson] = Field(default_factory=list)


class BookBlueprint(BaseModel):
    title: str
    curriculum: str
    stage: int
    term: int
    units: List[Unit] = Field(default_factory=list)
