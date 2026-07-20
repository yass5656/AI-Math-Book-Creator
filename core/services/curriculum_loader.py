from pathlib import Path
import yaml


class CurriculumLoader:

    def load(self, stage: int, term: int):

        path = Path(
            f"knowledge_base/Cambridge/Primary/Stage{stage}/Term{term}/book.yaml"
        )

        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
