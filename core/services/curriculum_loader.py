from pathlib import Path
import yaml


class CurriculumLoader:
    """
    Loads curriculum metadata from the Knowledge Base.

    Example:
    knowledge_base/
        Cambridge/
            Primary/
                Stage4/
                    Term1/
                        curriculum.yaml
    """

    BASE_PATH = Path("knowledge_base")

    def load(self, curriculum: str, stage: int, term: int):

        path = (
            self.BASE_PATH
            / curriculum
            / "Primary"
            / f"Stage{stage}"
            / f"Term{term}"
            / "curriculum.yaml"
        )

        if not path.exists():
            raise FileNotFoundError(
                f"Curriculum file not found:\n{path}"
            )

        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if data is None:
            raise ValueError(f"Empty curriculum file:\n{path}")

        return data
