from core.services.yaml_loader import YamlLoader
from core.generators import GENERATORS


class QuestionGenerator:

    def generate(self, pattern_path, difficulty="easy"):

        pattern = YamlLoader.load(pattern_path)

        generator = GENERATORS[pattern["generator"]]

        return generator.generate(pattern, difficulty)
