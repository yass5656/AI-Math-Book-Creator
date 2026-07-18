import random

from core.models.question import (
    Question,
    Difficulty,
    QuestionType,
)


class QuestionEngine:

    def generate_compare_negative_numbers(self):

        a = random.randint(-30, -1)
        b = random.randint(-30, -1)

        while a == b:
            b = random.randint(-30, -1)

        answer = "<" if a < b else ">"

        question = Question(
            question_id="AUTO-0001",
            curriculum="Cambridge",
            stage="Stage4",
            term=1,
            unit="Unit 1",
            learning_object="Negative Numbers",
            skill="Compare Negative Numbers",
            pattern_id="CMP001",
            difficulty=Difficulty.EASY,
            question_type=QuestionType.FILL_IN_THE_BLANK,
            question_text=f"{a} ____ {b}",
            answer=answer,
            workbook_style=True,
            progression_style=False,
            book_style=True
        )

        return question
