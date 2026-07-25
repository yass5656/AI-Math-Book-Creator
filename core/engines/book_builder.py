from core.models.book import Book
from core.engines.page_builder import PageBuilder
from core.services.unit_loader import UnitLoader
from core.engines.lesson_builder import LessonBuilder
from core.engines.test_builder import TestBuilder


class BookBuilder:

    def build(self, curriculum="Cambridge", stage=4, term=1):
        page_builder = PageBuilder()
        unit_loader = UnitLoader()
        lesson_builder = LessonBuilder()
        test_builder = TestBuilder()

        book = Book(
            title=f"Smart Start {curriculum} Mathematics Stage {stage} Term {term}",
            stage=stage,
            term=term
        )

        units = unit_loader.load_units(curriculum, stage, term)
        completed_units = []

        for index, unit in enumerate(units[:6], start=1):
            lesson = lesson_builder.build(
                lesson_title=f"Unit {index}",
                objectives=unit.get("objectives", [])
            )

            page = page_builder.build(
                title=f"Unit {index}",
                pattern=unit.get("pattern", ""),
                count=20,
                difficulty="easy",
                page_type="practice"
            )

            page.lesson_structure = lesson
            completed_units.append(index)
            page.progression_test = test_builder.build_progression_test(
                completed_units.copy()
            )

            book.pages.append(page)

        final_test = page_builder.build(
            title="Final Term Assessment",
            count=0,
            page_type="test",
            content=test_builder.build_final_term_test(6)
        )

        book.pages.append(final_test)

        return book
