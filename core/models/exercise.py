from dataclasses import dataclass

@dataclass
class Exercise:

    question: str

    answer: str

    difficulty: str

    marks: int = 1
