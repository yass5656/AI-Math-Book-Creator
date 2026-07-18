from config.settings import Settings


def main():

    settings = Settings()

    print(settings.project_name)

    print(settings.version)


if __name__ == "__main__":
    main()
