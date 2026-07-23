from core.engines.lesson_planner import LessonPlan


class LessonService:

    def create_default_plan(self):

        return LessonPlan(

            lesson_name="Negative Numbers",

            easy=20,

            medium=20,

            hard=10,

            workbook=15,

            progression=15,

            challenge=5

        )
