from dataclasses import dataclass, field
from typing import List


@dataclass
class PagePlan:
    page_number: int
    title: str
    page_type: str
    estimated_questions: int


@dataclass
class LessonPlan:
    lesson_name: str
    pages: List[PagePlan] = field(default_factory=list)


@dataclass
class UnitPlan:
    unit_name: str
    lessons: List[LessonPlan] = field(default_factory=list)


@dataclass
class BookPlan:
    title: str
    stage: str
    term: int
    book_type: str
    units: List[UnitPlan] = field(default_factory=list)


class BookPlanner:

    def create_lesson_plan(self, lesson_name: str):

        pages = [

            PagePlan(
                1,
                "Quick Review",
                "review",
                6
            ),

            PagePlan(
                2,
                "Worked Examples",
                "examples",
                2
            ),

            PagePlan(
                3,
                "Practice",
                "practice_easy",
                10
            ),

            PagePlan(
                4,
                "Practice",
                "practice_medium",
                10
            ),

            PagePlan(
                5,
                "Progression Practice",
                "progression",
                6
            ),

            PagePlan(
                6,
                "Homework",
                "homework",
                8
            )

        ]

        return LessonPlan(
            lesson_name=lesson_name,
            pages=pages
        )
