import yaml

from util.util import if_error_exit, if_file_not_exists_exit, file_content


class Bootstrap:
    def __init__(self, root_path, data_path) -> None:
        self.root_path = root_path
        self.data_path = data_path
        self.cfg = {}

    def execute(self):
        self.__config_yaml__()
        self.__table_json__()
        self.__datatypes__()

        return self.cfg

    # Valida se existe o arquivo yaml de configuração
    def __config_yaml__(self):
        file_yaml_name = 'config.yaml'
        file_yaml = self.root_path / file_yaml_name

        if_file_not_exists_exit(file_yaml)

        with open(file_yaml, 'r') as arquivo:
            self.dados_yaml = yaml.safe_load(arquivo)

    # valida se está configurado o arquivo que contém as configurações de tabelas
    def __table_json__(self):
        if_error_exit('file_table' not in self.dados_yaml, ERRO_FILE_TABLE)

        file_table = self.data_path / self.dados_yaml['file_table']

        if_file_not_exists_exit(file_table)

        self.cfg['file_table'] = file_table

    # faz o mapeamentO das colunas do banco de dados com o tipo para a linguagem de geração
    def __datatypes__(self):
        if_error_exit('template' not in self.dados_yaml, ERRO_TEMPLATE)

        def flag(x, y=self.dados_yaml): return y.get(
            'template', '') == '' or y['template'].get(x) == ''

        if_error_exit(flag('language'), ERRO_LANGUAGE)

        if_error_exit(flag('map_datatype'), ERRO_DATATYPE)

        file_datatype = self.data_path / \
            self.dados_yaml['template']['language'] / \
            self.dados_yaml['template']['map_datatype']

        if_file_not_exists_exit(file_datatype)

        self.cfg['datatypes'] = file_content(file_datatype)


ERRO_TEMPLATE = "A chave template não foi encontrada no arquivo config.yaml."
ERRO_FILE_TABLE = "A chave 'file_table' não foi encontrada no arquivo config.yaml."
ERRO_LANGUAGE = "A linguagem de geração não está definida no arquivo config.yaml."
ERRO_DATATYPE = "O arquivo de mapeamento dos datatypes não está definida no arquivo config.yaml."
