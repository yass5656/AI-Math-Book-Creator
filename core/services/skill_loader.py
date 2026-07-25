from pathlib import Path

from core.models.skill import Skill
from core.services.yaml_loader import YamlLoader


class SkillLoader:

    def load(self, unit_path):

        unit_path = Path(unit_path)

        skills_index = unit_path / "skills.yaml"

        if not skills_index.exists():
            return []

        index = YamlLoader.load(skills_index)

        loaded_skills = []

        for item in index.get("skills", []):

            skill_file = (
                unit_path
                / "skills"
                / f"{item['id']}.yaml"
            )

            if not skill_file.exists():
                continue

            data = YamlLoader.load(skill_file)

            loaded_skills.append(
                Skill(**data)
            )

        return loaded_skills
