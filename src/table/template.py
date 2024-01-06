class TemplateRow:
    def __init__(self, name, prefix, sufix, folder, fix=None) -> None:
        self.name=name
        self.prefix=prefix
        self.sufix=sufix
        self.folder=folder
        self.fix=fix


class Template:
    def __init__(self, fileTemlate) -> None:
        self.fileTemlate=fileTemlate

    def execute(self):
        print(self.fileTemlate)