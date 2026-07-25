class LessonBuilder:

    def build(self, lesson_title, objectives=None):
        return {
            "title": lesson_title,
            "sections": {
                "learning_objectives": objectives or [],
                "warm_up": [],
                "concept_explanation": [],
                "worked_examples": [],
                "practice": {
                    "level_1": [],
                    "level_2": [],
                    "level_3": []
                },
                "challenge": [],
                "review": []
            }
        }
