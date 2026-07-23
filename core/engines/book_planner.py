from core.models.book import Book

class BookPlanner:

    def create(self, title, stage, term):

        return Book(
            title=title,
            stage=stage,
            term=term
        )
