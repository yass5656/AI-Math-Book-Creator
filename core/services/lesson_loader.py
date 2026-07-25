from pathlib import Path
import yaml


class LessonLoader:

    def load_lessons(self, unit_path):

        lessons = []

        lessons_path = Path(unit_path) / "lessons"

        if not lessons_path.exists():
            return lessons

        for file in sorted(lessons_path.glob("*.yaml")):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:
                lessons.append(
                    yaml.safe_load(f)
                )

        return lessons
