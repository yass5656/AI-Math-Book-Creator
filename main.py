from core.engines.book_builder import BookBuilder
from core.services.book_exporter import BookExporter


def main():

    builder = BookBuilder()

    book = builder.build()

    exporter = BookExporter()

    exporter.export_json(

        book,

        "output/Stage4_Practice_Book.json"

    )

    print("Book exported successfully.")


if __name__ == "__main__":

    main()
