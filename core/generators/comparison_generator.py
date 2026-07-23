import random


class ComparisonGenerator:

    def generate(self, pattern, difficulty):

        limits = pattern["difficulty"][difficulty]

        a = random.randint(limits["min"], limits["max"])
        b = random.randint(limits["min"], limits["max"])

        operator = "<" if a < b else ">"
        question_type = pattern["question_type"]

        if question_type == "FillBlank":

            question = (
                pattern["template"]
                .replace("{A}", str(a))
                .replace("{B}", str(b))
            )

            answer = operator

        elif question_type == "MultipleChoice":

            question = (
                pattern["template"]
                .replace("{A}", str(a))
                .replace("{B}", str(b))
            )

            answer = operator

            choices = ["<", ">", "="]
            random.shuffle(choices)

            return {
                "question": question,
                "choices": choices,
                "answer": answer
            }

        elif question_type == "TrueFalse":

            shown_operator = random.choice(["<", ">"])

            question = (
                pattern["template"]
                .replace("{A}", str(a))
                .replace("{B}", str(b))
                .replace("{OP}", shown_operator)
            )

            answer = (shown_operator == operator)

        else:

            raise ValueError(f"Unsupported question type: {question_type}")

        return {
            "question": question,
            "answer": answer
        }
