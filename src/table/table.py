import json
import sys
from util.util import extrair_numeros


class TableColumn:
    def __init__(self, name, datatype, attribute, nn) -> None:
        self.name = name
        self.datatype = datatype
        self.attribute = attribute
        self.nn = nn
        self.size = extrair_numeros(datatype)
        self.auto_increment = attribute.lower().find('auto_increment') != -1
        self.primary = self.auto_increment or attribute.lower().find('primary_key') != -1
        self.unique = attribute.lower().find('unique') != -1


class TableData:
    def __init__(self, table_name, columns) -> None:
        self.name = table_name
        self.columns = columns


def LoadTable(path_table_json, tableName):

    try:
        filejson = open(path_table_json)
        data = json.load(filejson)
    finally:
        filejson.close()

    table = None

    # localiza a tabela
    for table_data in data:
        table_name = table_data.get("table")
        columns_data = table_data.get("columns", None)
        if columns_data is None:
            print("Propriedade coluna não foi encontrada")
            sys.exit()

        if table_name.lower().find(tableName.lower()) != -1:

            table_columns_list = []
            for column_data in columns_data:
                table_column = TableColumn(
                    name=column_data["name"],
                    datatype=column_data["datatype"],
                    attribute=column_data["attribute"],
                    nn=column_data["nn"]
                )
                table_columns_list.append(table_column)

            table = TableData(table_name, table_columns_list)
            break

    return table
