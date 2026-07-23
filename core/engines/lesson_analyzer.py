from core.models.lesson import Lesson


class LessonAnalyzer:


    def analyze(self, data):

        title = data["title"]

        objectives = data["objectives"]

        concepts = data["concepts"]


        lesson = Lesson(
            title=title,
            stage=4,
            objectives=objectives,
            concepts=concepts,
            examples=[],
            exercises=[]
        )

        return lesson
