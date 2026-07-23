from core.models.book import Book
from core.engines.page_builder import PageBuilder


class BookBuilder:

    def build(self):

        page_builder = PageBuilder()

        book = Book(
            title="Cambridge Stage 4 Practice Book",
            stage=4,
            term=1
        )

        pattern = (
            "knowledge_base/"
            "Cambridge/"
            "Primary/"
            "Stage4/"
            "Term1/"
            "Unit1/"
            "patterns/"
            "comparison/"
            "fill_blank.yaml"
        )

        page = page_builder.build(
            title="Compare Negative Numbers",
            pattern=pattern,
            count=20,
            difficulty="easy"
        )

        book.pages.append(page)

        return book
