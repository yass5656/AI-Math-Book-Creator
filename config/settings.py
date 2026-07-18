from pathlib import Path
import yaml


class Settings:

    def __init__(self):

        path = Path("config/project.yaml")

        with open(path, "r", encoding="utf-8") as f:

            self.data = yaml.safe_load(f)

    @property
    def project_name(self):

        return self.data["project"]["name"]

    @property
    def version(self):

        return self.data["project"]["version"]
