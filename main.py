from core.engines.question_generator import QuestionGenerator

generator = QuestionGenerator()

PATTERN = (
    "knowledge_base/"
    "Cambridge/Primary/"
    "Stage4/Term1/"
    "units/Unit1/"
    "patterns/CMP001.yaml"
)

for level in ["easy", "medium", "hard"]:

    print(f"\n===== {level.upper()} =====")

    for _ in range(5):

        q = generator.generate(PATTERN, level)

        print(q["question"], "Answer:", q["answer"])
