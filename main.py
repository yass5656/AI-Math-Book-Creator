from core.engines.question_engine import QuestionEngine


def main():

    engine = QuestionEngine()

    question = engine.generate_compare_negative_numbers()

    print(question.model_dump())


if __name__ == "__main__":
    main()
