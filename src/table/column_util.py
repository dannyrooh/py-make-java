import ast


class ColumnUtil:

    def __init__(self, datatypes) -> None:

        # Converte  str para o dict
        self.datatypes = ast.literal_eval(datatypes)

    def data_type(self, d):

        data_get = self.datatypes.get(d, None)
        if data_get is not None:
            return data_get

        if any(data_type in d for data_type in ['smallint', 'integer', 'int', 'long', 'bit']):
            return 'Integer'
        elif 'varchar' in d:
            return 'String'
        elif "date" in d:
            return "Date"
        elif "float" in d:
            return "Float"  
        else:
            return None
        
    def __private_column(self, m) :
         return m[0].lower() + m[1:]

    def column_private(self, column):
        col_type = self.data_type(column.datatype)
        name = column.name if column.entity is None else column.entity
        return f"private {col_type} {self.__private_column(name)};"
    
    

    def private_row(self, column):
        return f"\n{IDENT}{self.column_private(column)}\n"


IDENT = (' ' * 4)
