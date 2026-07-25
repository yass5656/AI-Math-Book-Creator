from core.services.curriculum_loader import CurriculumLoader


class CurriculumEngine:
    def __init__(self):
        self.loader = CurriculumLoader()

    def create_book_plan(self, curriculum="Cambridge", stage=4, term=1):
        data = self.loader.load(curriculum, stage, term)

        return {
            "curriculum": curriculum,
            "stage": stage,
            "term": term,
            "curriculum_data": data,
        }
