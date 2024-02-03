import json
import sys
from util.util import extrair_numeros

class TableColumn:
    def __init__(self, name, entity, datatype, attribute, nn) -> None:
        self.name = name
        self.datatype = datatype
        self.attribute = attribute
        self.entity = entity
        self.nn = nn
        self.size = extrair_numeros(datatype)
        self.auto_increment = attribute.lower().find('auto_increment') != -1
        self.primary = self.auto_increment or attribute.lower().find('primary_key') != -1
        self.unique = attribute.lower().find('unique') != -1

class TableData:

    name: str
    col_prefix: str
    columns: []

    def __init__(self, table_name, col_prefix, columns) -> None:
        self.name = table_name
        self.columns = columns
        self.col_prefix = col_prefix


def load_table(path_table_json, table_filter):

    try:
        filejson = open(path_table_json)
        data = json.load(filejson)
    finally:
        filejson.close()

    table = None

    # localiza a tabela
    for table_data in data:
        table_name = table_data.get("table")
        col_prefix = table_data.get("col_prefix")
        columns_data = table_data.get("columns", None)
        if columns_data is None:
            print("Propriedade coluna não foi encontrada")
            sys.exit()

        # if table_name.lower().find(tableName.lower()) != -1:
        if table_name.lower() == table_filter.lower():

            table_columns_list = []
            for column_data in columns_data:
                table_column = TableColumn(
                    name=column_data["name"],
                    entity=column_data.get("entity"),
                    datatype=column_data["datatype"],
                    attribute=column_data["attribute"],
                    nn=column_data["nn"]
                )
                table_columns_list.append(table_column)

            table = TableData(table_name, col_prefix, table_columns_list)
            break

    return table
