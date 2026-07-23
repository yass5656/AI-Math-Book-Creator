import json
from pathlib import Path


class BookExporter:

    def export_json(self, book, output_file):

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        data = {

            "title": book.title,

            "stage": book.stage,

            "term": book.term,

            "pages": []

        }

        for page in book.pages:

            page_data = {

                "title": page.title,

                "questions": []

            }

            for ex in page.exercises:

                page_data["questions"].append({

                    "id": ex.id,

                    "question": ex.question,

                    "answer": ex.answer,

                    "difficulty": ex.difficulty,

                    "marks": ex.marks

                })

            data["pages"].append(page_data)

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )
