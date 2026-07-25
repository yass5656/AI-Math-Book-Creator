from core.models.page import Page
from core.models.exercise import Exercise
from core.engines.question_generator import QuestionGenerator


class PageBuilder:

    def __init__(self):
        self.generator = QuestionGenerator()

    def build(
        self,
        title,
        pattern="",
        count=20,
        difficulty="easy",
        page_type="practice",
        content=None
    ):
        page = Page(
            title=title,
            content=content or {},
            page_type=page_type
        )

        used_questions = set()
        index = 0

        while index < count and pattern:
            question = self.generator.generate(
                pattern,
                difficulty
            )

            if question["question"] in used_questions:
                continue

            used_questions.add(question["question"])

            page.exercises.append(
                Exercise(
                    id=f"Q{index + 1}",
                    question=question["question"],
                    answer=question["answer"],
                    marks=1,
                    difficulty=difficulty,
                    source=pattern
                )
            )

            index += 1

        return page
