from core.models.page import Page
from core.models.exercise import Exercise
from core.engines.question_generator import QuestionGenerator


class PageBuilder:

    def build(self, title, pattern, count):

        generator = QuestionGenerator()

        page = Page(title)

        for _ in range(count):

            q = generator.generate(pattern)

            page.exercises.append(

                Exercise(

                    question=q["question"],

                    answer=q["answer"],

                    difficulty="Easy"

                )

            )

        return page
