from pathlib import Path
import yaml


class UnitLoader:

    BASE_PATH = Path("knowledge_base")

    def load_units(self, curriculum, stage, term):

        units_path = (
            self.BASE_PATH
            / curriculum
            / "Primary"
            / f"Stage{stage}"
            / f"Term{term}"
            / "units"
        )

        if not units_path.exists():
            raise FileNotFoundError(
                f"Units folder not found: {units_path}"
            )

        units = []

        for unit_folder in sorted(units_path.iterdir()):

            if unit_folder.is_dir():

                unit_file = unit_folder / "unit.yaml"

                data = {}

                if unit_file.exists():

                    with open(
                        unit_file,
                        "r",
                        encoding="utf-8"
                    ) as file:
                        data = yaml.safe_load(file) or {}

                data["path"] = str(unit_folder)

                units.append(data)

        return units
