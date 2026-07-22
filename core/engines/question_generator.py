from pathlib import Path
import random
import yaml


class QuestionGenerator:

    def generate(self):

        pattern_file = Path(
            "knowledge_base/Cambridge/Primary/Stage4/Term1/units/Unit1/patterns/CMP001.yaml"
        )

        with open(pattern_file, encoding="utf-8") as f:
            pattern = yaml.safe_load(f)

        r = pattern["range"]["easy"]

        a = random.randint(r["min"], r["max"])
        b = random.randint(r["min"], r["max"])

        answer = "<" if a < b else ">"

        question = pattern["template"]["question"]

        question = question.replace("{A}", str(a))
        question = question.replace("{B}", str(b))

        return {

            "question": question,

            "answer": answer

        }
