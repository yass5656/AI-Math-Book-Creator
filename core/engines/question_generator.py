from pathlib import Path

from core.services.yaml_loader import YamlLoader
from core.generators import GENERATORS


class QuestionGenerator:

    def generate(self, pattern_path, difficulty="easy"):

        pattern_path = Path(pattern_path)

        if not pattern_path.exists():
            raise FileNotFoundError(f"Pattern file not found: {pattern_path}")

        pattern = YamlLoader.load(pattern_path)

        generator_name = pattern.get("generator")

        if generator_name not in GENERATORS:
            raise ValueError(f"Unknown generator: {generator_name}")

        generator = GENERATORS[generator_name]

        return generator.generate(pattern, difficulty)
