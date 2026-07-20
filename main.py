from core.services.curriculum_loader import CurriculumLoader

loader = CurriculumLoader()

book = loader.load(4, 1)

print(book["title"])

for unit in book["units"]:
    print(unit["name"])

    for lesson in unit["lessons"]:
        print("   -", lesson["name"])
