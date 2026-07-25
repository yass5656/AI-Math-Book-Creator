from core.models.book import Book
from core.models.page import Page
from core.engines.lesson_builder import LessonBuilder
from core.engines.test_builder import TestBuilder
from core.services.unit_loader import UnitLoader
from core.services.lesson_loader import LessonLoader


class BookBuilder:

    def build(self, curriculum="Cambridge", stage=4, term=1):

        unit_loader = UnitLoader()
        lesson_loader = LessonLoader()
        lesson_builder = LessonBuilder()
        test_builder = TestBuilder()

        book = Book(
            title=f"Smart Start {curriculum} Mathematics Stage {stage} Term {term}",
            stage=stage,
            term=term
        )

        units = unit_loader.load_units(
            curriculum,
            stage,
            term
        )

        completed_units = []

        for index, unit in enumerate(units[:6], start=1):

            lessons = lesson_loader.load_lessons(
                unit["path"]
            )

            for lesson in lessons:

                lesson_data = lesson_builder.build(
                    lesson_title=lesson["title"],
                    objectives=lesson.get(
                        "objectives",
                        []
                    )
                )

                lesson_data["warm_up"] = lesson.get(
                    "warm_up",
                    []
                )

                lesson_data["concept_explanation"] = lesson.get(
                    "concept_explanation",
                    []
                )

                lesson_data["worked_examples"] = lesson.get(
                    "worked_examples",
                    []
                )

                page = Page(
                    title=lesson["title"],
                    content=lesson_data,
                    page_type="lesson"
                )

                book.pages.append(page)

            completed_units.append(index)

            test_page = Page(
                title=f"Progression Test {index}",
                content=test_builder.build_progression_test(
                    completed_units.copy()
                ),
                page_type="test"
            )

            book.pages.append(test_page)

        return book
