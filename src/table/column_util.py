import ast


class ColumnUtil:

    def __init__(self, datatypes) -> None:

        # Converte  str para o dict
        self.datatypes = ast.literal_eval(datatypes)

    def data_type(self, d):

        dataGet = self.datatypes.get(d, None)
        if not dataGet is None:
            return dataGet

        if any(data_type in d for data_type in ['smallint', 'int', 'long']):
            return 'Integer'
        elif 'varchar' in d:
            return 'String'
        else:
            return None

    def column_private(self, column):
        col_type = self.data_type(column.datatype)
        return f"private {col_type} {column.name.lower()};"

    def private_row(self, column):
        return f"\n{IDENT}{self.column_private(column)}\n"


IDENT = (' ' * 4)
