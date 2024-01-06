import sys
from config.config import ROOT_PATH, DATA_PATH
from config.bootstrap import Bootstrap

from util.util import if_error_exit

from table.table import LoadTable

cfg_path = Bootstrap(ROOT_PATH, DATA_PATH).execute()

# nome da tabela informada pelo usuário
tableName = sys.argv[1] if len(sys.argv) > 1 else None

if_error_exit(tableName is None,
              "Desenvolvedor, informe o nome da tabela!\nexemplo: py main.py <nome_da_tabela>")

table = LoadTable(cfg_path['file_table'], tableName)

file_table = cfg_path['file_table']
if_error_exit(table is None,
              f'A tabela informada "{tableName}" não está presente no arquivo "{file_table}"')
if_error_exit(len(table.columns) == 0,
              f'A propriedade coluna deve ter ao menos 1 coluna definida no arquivo \n"{file_table}"')
