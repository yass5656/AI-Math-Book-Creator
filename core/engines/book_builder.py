from core.models.book import Book
from core.engines.page_builder import PageBuilder
from core.engines.curriculum_engine import CurriculumEngine


class BookBuilder:

    def build(self, curriculum="Cambridge", stage=4, term=1):
        page_builder = PageBuilder()
        curriculum_engine = CurriculumEngine()

        plan = curriculum_engine.create_book_plan(
            curriculum=curriculum,
            stage=stage,
            term=term
        )

        book = Book(
            title=f"{curriculum} Stage {stage} Practice Book",
            stage=stage,
            term=term
        )

        # Temporary compatibility with current generator.
        # Unit iteration will replace this in the next phase.
        pattern = (
            "knowledge_base/"
            f"{curriculum}/"
            "Primary/"
            f"Stage{stage}/"
            f"Term{term}/"
            "units/Unit1/patterns/comparison/fill_blank.yaml"
        )

        page = page_builder.build(
            title="Compare Negative Numbers",
            pattern=pattern,
            count=20,
            difficulty="easy"
        )

        book.pages.append(page)

        return book
