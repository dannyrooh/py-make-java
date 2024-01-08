from pathlib import Path
import yaml


class FileUtil:

    def __init__(self, filePath, sobrescrever=True) -> None:
        self.path = Path(filePath)
        self.sobrescrever = sobrescrever

    def create(self, fileName, contentBody=None):
        file = (self.path / fileName)

        # cria o direteorio se não existe
        file.parent.mkdir(parents=True, exist_ok=True)

        # criar ou sobscreve o arquivo existente
        if (not self.sobrescrever) and file.exists():
            return

        body = '' if contentBody is None else contentBody

        with open(file, "w") as myfile:
            myfile.write(body)

        return file


def file_content(filepath, msg_erro=None):
    try:
        file = open(filepath, 'r')
        file_content = file.read()

        if not (file_content):
            raise Exception(
                msg_erro if msg_erro is None else f'Arquivo não encontrado /n {filepath}')

        return file_content
    finally:
        file.close()


def file_yaml(filepath, msg_erro=None):
    try:
        with open(filepath, 'r') as file:
            file_content = yaml.safe_load(file)

        if not (file_content):
            raise Exception(
                msg_erro if msg_erro is None else f'Arquivo não encontrado /n {filepath}')

        return file_content
    finally:
        file.close()
