from pathlib import Path
import yaml


class PatternLoader:

    def __init__(self, unit_path):

        self.pattern_root = Path(unit_path) / "patterns"

        self.index = yaml.safe_load(
            (self.pattern_root / "index.yaml").read_text(
                encoding="utf-8"
            )
        )

    def load(self, pattern_id):

        relative_path = self.index[pattern_id]

        with open(
            self.pattern_root / relative_path,
            encoding="utf-8"
        ) as f:

            return yaml.safe_load(f)
