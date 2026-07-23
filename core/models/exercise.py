from dataclasses import dataclass

@dataclass
class Exercise:
    id: str
    question: str
    answer: str
    marks: int
    difficulty: str
    source: str
