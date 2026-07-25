from core.engines.book_builder import BookBuilder
from core.services.book_exporter import BookExporter


CONFIG = {
    "curriculum": "Cambridge",
    "stage": 4,
    "term": 1
}


def main():

    builder = BookBuilder()

    book = builder.build(
        curriculum=CONFIG["curriculum"],
        stage=CONFIG["stage"],
        term=CONFIG["term"]
    )

    exporter = BookExporter()

    exporter.export_json(
        book,
        f"output/{CONFIG['curriculum']}_Stage{CONFIG['stage']}_Term{CONFIG['term']}.json"
    )

    print("Book exported successfully.")


if __name__ == "__main__":
    main()
