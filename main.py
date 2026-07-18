from core.models.question import Question, Difficulty, QuestionType


def main():
    question = Question(
        question_id="S4-T1-U1-0001",
        curriculum="Cambridge",
        stage="Stage4",
        term=1,
        unit="Unit 1",
        learning_object="Negative Numbers",
        skill="Compare Negative Numbers",
        pattern_id="CMP001",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.FILL_IN_THE_BLANK,
        question_text="Compare: -8 ___ -3",
        answer="<",
        workbook_style=True,
        progression_style=False,
        book_style=True
    )

    print(question.model_dump())


if __name__ == "__main__":
    main()
