from pydantic import BaseModel


class BookRequest(BaseModel):
    curriculum: str
    stage: int
    term: int
    book_type: str
    theme: str
    language: str = "English"
