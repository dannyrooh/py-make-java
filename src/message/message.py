MSG_ERRO_PARAM_TABELA = "Desenvolvedor, informe o nome da tabela!\nexemplo: py main.py <nome_da_tabela>"


def MSG_ERRO_TABLE_NOT_FOUND(
    tableName, file_table): return f'A tabela informada "{tableName}" não está presente no arquivo "{file_table}"'


def MSG_ERRO_COLUMNS(
    file_table): return f'A propriedade coluna deve ter ao menos 1 coluna definida no arquivo \n"{file_table}"'
