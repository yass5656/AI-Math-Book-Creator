from core.engines.book_builder import BookBuilder

book = BookBuilder().build()

print(book.title)

print()

for page in book.pages:

    print(page.title)

    print("-"*40)

    for i, ex in enumerate(page.exercises,1):

        print(i, ex.question)
