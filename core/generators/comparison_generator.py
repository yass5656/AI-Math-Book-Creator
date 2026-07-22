import random


class ComparisonGenerator:

    def generate(self, pattern, difficulty):

        limits = pattern["difficulty"][difficulty]

        a = random.randint(limits["min"], limits["max"])
        b = random.randint(limits["min"], limits["max"])

        operator = "<" if a < b else ">"

        question = (
            pattern["template"]
            .replace("{A}", str(a))
            .replace("{B}", str(b))
        )

        return {

            "question": question,

            "answer": operator

        }
