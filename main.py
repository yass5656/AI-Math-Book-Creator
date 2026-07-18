from core.engines.book_planner import BookPlanner


def main():

    planner = BookPlanner()

    lesson = planner.create_lesson_plan(
        "Negative Numbers"
    )

    print(lesson)


if __name__ == "__main__":
    main()
