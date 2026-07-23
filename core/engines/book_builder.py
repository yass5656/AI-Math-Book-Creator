from core.models.book import Book
from core.engines.page_builder import PageBuilder
from core.services.curriculum_loader import CurriculumLoader


class BookBuilder:

    def build(
        self,
        curriculum="Cambridge",
        stage=4,
        term=1,
    ):

        loader = CurriculumLoader()
        curriculum_data = loader.load(curriculum, stage, term)

        builder = PageBuilder()

        book = Book(
    title=curriculum_data["title"],
    stage=stage,
    term=term
)

        for unit in curriculum_data["units"]:

            for page in unit["pages"]:

                book.pages.append(
                    builder.build(
                        title=page["title"],
                        pattern=page["pattern"],
                        count=page["count"],
                        difficulty=page.get("difficulty", "easy"),
                    )
                )

        return book
