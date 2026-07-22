from core.engines.question_generator import QuestionGenerator

generator = QuestionGenerator()

for i in range(10):

    q = generator.generate()

    print(q["question"], " Answer:", q["answer"])
