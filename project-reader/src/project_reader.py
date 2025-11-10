from urllib import request
from project import Project
import tomlkit
import os


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = os.path.expanduser(self._url)
        content = os.path.normpath(content)

        with open(content, "r", encoding="utf-8") as f: content = f.read()

        print(content)

        data = tomlkit.parse(content)
        tool_data = data["tool"]["poetry"]

        name = tool_data.get("name", "Projekti")
        description = tool_data.get("description", "Ei kuvausta")
        licence = tool_data.get("licence", "Ei lisenssiä")

        authors_raw = tool_data.get("authors", [])
        authors = []
        for author in authors_raw:
            if "<" in author:
                author = author.split("<")[0].strip()
            authors.append(author)

        dependencies = list(tool_data.get("dependencies", {}).keys())
        dev_dependencies = list(tool_data.get("dev-dependencies", {}).keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, licence, authors, dependencies, dev_dependencies)
