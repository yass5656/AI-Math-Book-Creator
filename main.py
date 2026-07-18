from agents.knowledge_builder.knowledge_builder import KnowledgeBuilder


def main():

    builder = KnowledgeBuilder()

    builder.run(

        stage=4,

        term=1,

        unit="Numbers",

        lesson="Negative Numbers"

    )


if __name__ == "__main__":
    main()
