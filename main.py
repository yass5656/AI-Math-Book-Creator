from core.engines.book_builder import BookBuilder


def main():

    builder = BookBuilder()

    book = builder.build()

    print(f"\n{book.title}")
    print("=" * len(book.title))

    for page in book.pages:

        print(f"\n{page.title}")
        print("-" * 40)

        for i, exercise in enumerate(page.exercises, start=1):
            print(f"{i}. {exercise.question}")


if __name__ == "__main__":
    main()
