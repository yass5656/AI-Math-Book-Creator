class PromptBuilder:

    def build_skill_prompt(
        self,
        stage,
        term,
        unit,
        lesson
    ):

        return f"""
You are an experienced Cambridge Mathematics curriculum specialist.

Curriculum:
Cambridge Primary Mathematics

Stage:
{stage}

Term:
{term}

Unit:
{unit}

Lesson:
{lesson}

Return ONLY JSON.

Extract:

1 Skills

2 Learning Objectives

3 Vocabulary

4 Common Misconceptions

5 Progression Style Question Types

6 Workbook Style Question Types

7 Suggested Teaching Order
"""
