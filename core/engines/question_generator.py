import random

from core.services.yaml_loader import YamlLoader


class QuestionGenerator:

    def generate(self, pattern_path, difficulty="easy"):

        pattern = YamlLoader.load(pattern_path)

        limits = pattern["range"][difficulty]

        a = random.randint(limits["min"], limits["max"])
        b = random.randint(limits["min"], limits["max"])

        answer = "<" if a < b else ">"

        question = (
            pattern["template"]["question"]
            .replace("{A}", str(a))
            .replace("{B}", str(b))
        )

        return {
            "question": question,
            "answer": answer,
            "pattern": pattern["id"],
            "difficulty": difficulty,
        }
