from pathlib import Path

from core.services.yaml_loader import YamlLoader


class PatternLoader:

    def load(self, unit_path, pattern_ids):

        unit_path = Path(unit_path)

        patterns = []

        for pattern_id in pattern_ids:

            pattern_file = (
                unit_path
                / "patterns"
                / f"{pattern_id}.yaml"
            )

            if not pattern_file.exists():
                continue

            patterns.append(
                YamlLoader.load(pattern_file)
            )

        return patterns
