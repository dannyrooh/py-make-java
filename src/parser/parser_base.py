from util.file_util import FileUtil, file_content
from util.util import if_file_not_exists_exit
from table.column_util import ColumnUtil


class ParserBase:
    def __init__(self) -> None:
        self.var_template = {}

    def execute(self, config):
        self.path_destiny = config['path_destiny']
        self.templates = config['templates']
        self.package_path = config['package_path']
        self.table = config['table']
        self.datatypes = config['datatypes']

    def file_create(self, file_name, content_body=None, sobrescrever=True):
        util = FileUtil(self.path_destiny, sobrescrever)
        return util.create(file_name,
                           '' if content_body is None else content_body)

    def load_file(self, file_path):
        if_file_not_exists_exit(file_path)
        return file_content(file_path)

    def parse_template(self, file_path):
        template = self.load_file(file_path)
        var_mapper = {}
        for k, v in self.var_template.items():
            x = "{"+k+"}"
            if x in template:
                var_mapper[k] = v
        if len(var_mapper) == 0:
            return template
        else:
            content_body = template.format(**var_mapper)
            return content_body
        
    def __column_data__(self, column):
        nn = 'false' if column.nn else 'true'
        length = ''
        if (column.size is not None) and (column.size > 0):
            length = f' , length = {column.size}'

        name =  column.name if column.entity is None else column.entity

        return f'@Column(name = "{name}", nullable = {nn}{length})'        

    def __body_columns__(self, cadastra=False):
        column_util = ColumnUtil(self.datatypes)
        cols = ''
        for column in self.table.columns:
            if (cadastra and (not column.auto_increment)) or (not cadastra):
                cols += column_util.private_row(column)
        return cols

    def __body_jpa__(self, cadastra=False):
        column_util = ColumnUtil(self.datatypes)
        self.cols = ''
        def add(value):
            self.cols += f'{IDENT}{value}\n'

        for column in self.table.columns:
            name =  column.name if column.entity is None else column.entity
            if name.lower() == 'id':
                add('@Id')
                if column.auto_increment:
                    add('@GeneratedValue(strategy = GenerationType.IDENTITY)')
                add(self.__column_data__(column))
                add(column_util.column_private(column))
                add('')
            else:
                add(self.__column_data__(column))
                add(column_util.column_private(column))
                add('')
        return self.cols


    def __datatype_id__(self):
        column_util = ColumnUtil(self.datatypes)
        did = ''
        for column in self.table.columns:
            name =  column.name if column.entity is None else column.entity
            if (name.lower() == 'id' ):
                did = column_util.data_type(column.datatype)
                break

        return did

IDENT = (' '*4)