import json
from pathlib import Path


class KnowledgeWriter:

    def save(
        self,
        path,
        data
    ):

        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )
