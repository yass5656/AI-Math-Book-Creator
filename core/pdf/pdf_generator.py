import json
from pathlib import Path


class PDFGenerator:

    def generate(self, book, output_file):

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_file.replace(".pdf", ".json"),
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                book,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            "Smart Start prototype generated:",
            output_file
        )

