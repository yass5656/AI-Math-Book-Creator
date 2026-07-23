from core.models.page import Page
from core.models.exercise import Exercise
from core.engines.question_generator import QuestionGenerator


class PageBuilder:

    def __init__(self):
        self.generator = QuestionGenerator()

    def build(
        self,
        title,
        pattern,
        count,
        difficulty="easy"
    ):

        page = Page(title)

        for index in range(count):

            question = self.generator.generate(
                pattern,
                difficulty
            )

            page.exercises.append(

                Exercise(

                    id=f"Q{index+1}",

                    question=question["question"],

                    answer=question["answer"],

                    marks=1,

                    difficulty=difficulty,

                    source=pattern

                )

            )

        return page
