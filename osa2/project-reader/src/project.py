class Project:
    def __init__(self, name, description, licence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.licence = licence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_str = "\n".join(f"- {a}" for a in self.authors)
        return (
            f"Name: {self.name}\n"
            f"\nDescription: {self.description or '-'}\n"
            f"Licence: {self.licence}\n\n"
            f"Authors:\n{authors_str}\n\n"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}\n\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
