from core.models.book_request import BookRequest
from core.engines.book_planner import BookPlanner


request = BookRequest(
    curriculum="Cambridge",
    stage=4,
    term=1,
    book_type="Practice",
    theme="Modern Blue"
)

planner = BookPlanner()

book = planner.build(request)

print(book)
