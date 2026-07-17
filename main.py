from agents.planner_agent import create_plan


def main():

    plan = create_plan(
        "config/book_config.json"
    )

    print("Book Plan Created:")
    print(plan)


if __name__ == "__main__":
    main()
