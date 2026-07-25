class TestBuilder:

    def build_progression_test(self, units_completed):
        return {
            "type": "progression_test",
            "covers_units": units_completed,
            "questions": []
        }

    def build_final_term_test(self, total_units=6):
        return {
            "type": "final_term_test",
            "covers_units": list(range(1, total_units + 1)),
            "questions": []
        }
