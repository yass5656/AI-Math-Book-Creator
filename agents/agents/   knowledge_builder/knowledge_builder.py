from .prompt_builder import PromptBuilder


class KnowledgeBuilder:

    def run(
        self,
        stage,
        term,
        unit,
        lesson
    ):

        prompt = PromptBuilder().build_skill_prompt(
            stage,
            term,
            unit,
            lesson
        )

        print(prompt)
