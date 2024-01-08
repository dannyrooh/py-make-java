import sys
from config.config import ROOT_PATH, DATA_PATH, CUR_PATH
from config.bootstrap import Bootstrap
from message.message import MSG_ERRO_PARAM_TABELA, MSG_ERRO_TABLE_NOT_FOUND, MSG_ERRO_COLUMNS
from util.util import if_error_exit, if_isnone_exit

from table.table import LoadTable
from table.template import Template
from parser.bot import Bot

config = Bootstrap(ROOT_PATH, DATA_PATH).execute()

# nome da tabela informada pelo usuário
tableName = sys.argv[1] if len(sys.argv) > 1 else None
if_isnone_exit(tableName, MSG_ERRO_PARAM_TABELA)

table = LoadTable(config['file_table'], tableName)

file_table = config['file_table']
if_isnone_exit(table, MSG_ERRO_TABLE_NOT_FOUND(tableName, file_table))

if_error_exit(len(table.columns) == 0, MSG_ERRO_COLUMNS(file_table))

template_rows = Template(config).execute()

# print(template_list)
Bot(config['bot']).execute(template_rows, CUR_PATH, table, config['datatypes'])
