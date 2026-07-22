from core.models.book import Book
from core.engines.page_builder import PageBuilder


class BookBuilder:

    def build(self):

        pattern = (
            "knowledge_base/"
            "Cambridge/Primary/"
            "Stage4/Term1/"
            "units/Unit1/"
            "patterns/comparison/fill_blank.yaml"
        )

        builder = PageBuilder()

        book = Book("Stage 4 Practice Book")

        book.pages.append(

            builder.build(

                "Practice Page",

                pattern,

                20

            )

        )

        return book
