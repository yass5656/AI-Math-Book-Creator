from pathlib import Path

from core.models.skill import Skill
from core.services.yaml_loader import YamlLoader


class SkillLoader:

    def load(self, unit_path):

        unit_path = Path(unit_path)

        skills_file = unit_path / "skills.yaml"

        if not skills_file.exists():
            return []

        data = YamlLoader.load(skills_file)

        loaded_skills = []

        for item in data.get("skills", []):

            loaded_skills.append(
                Skill(
                    id=item["id"],

                    title=item.get(
                        "name",
                        item["id"]
                    ),

                    learning_objective=item.get(
                        "name",
                        ""
                    ),

                    generator=item.get(
                        "generator",
                        "comparison_generator"
                    ),

                    patterns=item.get(
                        "patterns",
                        []
                    )
                )
            )

        return loaded_skills
        