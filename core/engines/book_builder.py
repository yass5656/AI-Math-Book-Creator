import os

from core.models.book import Book
from core.models.page import Page

from core.services.unit_loader import UnitLoader
from core.services.skill_loader import SkillLoader
from core.services.lesson_loader import LessonLoader
from core.services.pattern_loader import PatternLoader

from core.engines.lesson_builder import LessonBuilder
from core.engines.question_generator import QuestionGenerator


class BookBuilder:

    def __init__(self):

        self.unit_loader = UnitLoader()
        self.skill_loader = SkillLoader()
        self.lesson_loader = LessonLoader()
        self.pattern_loader = PatternLoader()

        self.lesson_builder = LessonBuilder()
        self.question_generator = QuestionGenerator()


    def build(
        self,
        curriculum,
        stage,
        term
    ):

        book = Book(
            title=f"Smart Start Cambridge Stage {stage} Term {term}",
            stage=stage,
            term=term
        )


        units = self.unit_loader.load_units(
            curriculum,
            stage,
            term
        )


        completed_units = []


        for index, unit in enumerate(units[:6], start=1):

            print(
                "Processing unit:",
                unit.get("title")
            )


            # Build correct knowledge path
            unit_path = os.path.join(
                "knowledge_base",
                "Cambridge",
                "Primary",
                f"Stage{stage}",
                f"Term{term}",
                "units",
                unit["path"]
            )


            skills = self.skill_loader.load(
                unit_path
            )


            lessons = self.lesson_loader.load_lessons(
                unit_path
            )


            for lesson in lessons:


                lesson_data = self.lesson_builder.build(
                    lesson_title=lesson["title"],
                    objectives=lesson.get(
                        "objectives",
                        []
                    )
                )


                generated_questions = []


                for skill in skills:


                    for pattern_id in skill.patterns:


                        try:

                            patterns = self.pattern_loader.load(
                                unit_path,
                                [str(pattern_id)]
                            )


                            for pattern in patterns:

                                question = (
                                    self.question_generator.generate(
                                        pattern,
                                        "easy"
                                    )
                                )

                                generated_questions.append(
                                    question
                                )


                        except Exception as e:

                            print(
                                "Question generation error:",
                                e
                            )



                lesson_data["generated_questions"] = (
                    generated_questions
                )


                page = Page(
                    title=lesson["title"],
                    content=lesson_data,
                    page_type="lesson"
                )


                page.exercises = (
                    generated_questions
                )


                book.pages.append(
                    page
                )


            completed_units.append(
                index
            )


        print(
            "Completed units:",
            completed_units
        )


        return book
        