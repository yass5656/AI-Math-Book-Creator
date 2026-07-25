from pathlib import Path

from core.services.yaml_loader import YamlLoader
from core.generators import GENERATORS


class QuestionGenerator:

    def generate(
        self,
        pattern,
        difficulty="easy"
    ):

        # Support dictionary input
        # from PatternLoader
        if isinstance(pattern, dict):

            pattern_data = pattern

        else:

            # Support file path input
            pattern_path = Path(pattern)

            if not pattern_path.exists():
                raise FileNotFoundError(
                    f"Pattern file not found: {pattern_path}"
                )

            pattern_data = YamlLoader.load(
                pattern_path
            )


        generator_name = pattern_data.get(
            "generator"
        )


        if generator_name not in GENERATORS:

            raise ValueError(
                f"Unknown generator: {generator_name}"
            )


        generator = GENERATORS[
            generator_name
        ]


        return generator.generate(
            pattern_data,
            difficulty
        )
        