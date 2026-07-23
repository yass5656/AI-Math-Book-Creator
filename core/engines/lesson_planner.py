from dataclasses import dataclass


@dataclass
class LessonPlan:

    lesson_name: str

    easy: int

    medium: int

    hard: int

    workbook: int

    progression: int

    challenge: int
