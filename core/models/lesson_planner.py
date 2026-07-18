from core.models.book_blueprint import (
    Lesson,
    Page,
    QuestionBlock
)


class LessonPlanner:

    def build(self, lesson_name):

        lesson = Lesson(
            lesson_name=lesson_name
        )

        lesson.pages.append(
            Page(
                page_number=1,
                title="Guided Practice",
                blocks=[
                    QuestionBlock(
                        title="Easy Practice",
                        style="Workbook",
                        count=8,
                        difficulty="Easy"
                    ),
                    QuestionBlock(
                        title="Medium Practice",
                        style="Workbook",
                        count=8,
                        difficulty="Medium"
                    )
                ]
            )
        )

        lesson.pages.append(
            Page(
                page_number=2,
                title="Progression Practice",
                blocks=[
                    QuestionBlock(
                        title="Reasoning",
                        style="Progression",
                        count=6,
                        difficulty="Hard"
                    )
                ]
            )
        )

        return lesson
