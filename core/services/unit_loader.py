from pathlib import Path
import yaml


class UnitLoader:
    BASE_PATH = Path("knowledge_base")

    def load_units(self, curriculum, stage, term):
        path = (
            self.BASE_PATH / curriculum / "Primary" /
            f"Stage{stage}" / f"Term{term}" / "units"
        )

        if not path.exists():
            raise FileNotFoundError(f"Units folder not found: {path}")

        units = []
        for unit_file in path.rglob("*.yaml"):
            with open(unit_file, "r", encoding="utf-8") as file:
                units.append(yaml.safe_load(file))

        return units
