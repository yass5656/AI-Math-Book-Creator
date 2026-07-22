from core.engines.question_generator import QuestionGenerator

generator = QuestionGenerator()

question = generator.generate(

    "knowledge_base/Cambridge/Primary/Stage4/Term1/units/Unit1/patterns/comparison/fill_blank.yaml"

)

print(question)
