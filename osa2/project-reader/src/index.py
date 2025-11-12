from project_reader import ProjectReader


def main():
    url = "C:\\Users\\-Käyttäjä-\\Git\\osa2\\project-reader\\pyproject.toml"
    reader = ProjectReader(url)
    print(reader.get_project())


if __name__ == "__main__":
    main()
