import random


class ComparisonGenerator:

    def generate(self, pattern, difficulty):

        limits = pattern["difficulty"][difficulty]

        # منع توليد عددين متساويين
        while True:
            a = random.randint(limits["min"], limits["max"])
            b = random.randint(limits["min"], limits["max"])

            if a != b:
                break

        if a < b:
            operator = "<"
        elif a > b:
            operator = ">"
        else:
            operator = "="

        question_type = pattern["question_type"]

        if question_type == "FillBlank":

            question = (
                pattern["template"]
                .replace("{A}", str(a))
                .replace("{B}", str(b))
            )

            return {
                "question": question,
                "answer": operator
            }

        elif question_type == "MultipleChoice":

            question = (
                pattern["template"]
                .replace("{A}", str(a))
                .replace("{B}", str(b))
            )

            choices = ["<", ">", "="]
            random.shuffle(choices)

            return {
                "question": question,
                "choices": choices,
                "answer": operator
            }

        elif question_type == "TrueFalse":

            shown_operator = random.choice(["<", ">"])

            question = (
                pattern["template"]
                .replace("{A}", str(a))
                .replace("{B}", str(b))
                .replace("{OP}", shown_operator)
            )

            return {
                "question": question,
                "answer": (shown_operator == operator)
            }

        else:

            raise ValueError(
                f"Unsupported question type: {question_type}"
            )
