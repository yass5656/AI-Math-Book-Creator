import json


def create_plan(config_file):

    with open(config_file, "r") as file:
        config = json.load(file)

    plan = {
        "title": config["title"],
        "sections": [
            "Learning Objectives",
            "Warm Up Activity",
            "Concept Explanation",
            "Worked Examples",
            "Practice Questions",
            "Challenge Activity",
            "Review"
        ]
    }

    return plan
