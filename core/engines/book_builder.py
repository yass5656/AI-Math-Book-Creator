from core.models.book import Book
from core.engines.page_builder import PageBuilder
from core.services.unit_loader import UnitLoader


class BookBuilder:

    def build(self, curriculum="Cambridge", stage=4, term=1):
        page_builder = PageBuilder()
        unit_loader = UnitLoader()

        book = Book(
            title=f"Smart Start {curriculum} Mathematics Stage {stage} Term {term}",
            stage=stage,
            term=term
        )

        units = unit_loader.load_units(curriculum, stage, term)

        for index, unit in enumerate(units[:6], start=1):
            page = page_builder.build(
                title=f"Unit {index}",
                pattern=unit.get("pattern", ""),
                count=20,
                difficulty="easy"
            )

            book.pages.append(page)

        return book
