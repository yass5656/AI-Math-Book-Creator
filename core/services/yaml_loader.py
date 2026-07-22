from pathlib import Path
import yaml


class YamlLoader:

    @staticmethod
    def load(file_path):

        with open(Path(file_path), "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
