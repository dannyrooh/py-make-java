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

    def file_create(self, fileName, contentBody=None, sobrescrever=True):
        util = FileUtil(self.path_destiny, sobrescrever)
        return util.create(fileName,
                           '' if contentBody is None else contentBody)

    def load_file(self, filePath):
        if_file_not_exists_exit(filePath)
        return file_content(filePath)

    def parse_template(self, filePath):
        template = self.load_file(filePath)
        var_mapper = {}
        for k, v in self.var_template.items():
            x = "{"+k+"}"
            if x in template:
                var_mapper[k] = v
        if len(var_mapper) == 0:
            return template
        else:
            contentBody = template.format(**var_mapper)
            return contentBody
        
    def __column_data__(self, column):
        nn = 'false' if column.nn else 'true'
        length = ''
        if (not column.size is None) and (column.size > 0):
            length = f' , length = {column.size}'

        return f'@Column(name = "{column.name}", nullable = {nn}{length})'        

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
            if column.name.lower() == 'id':
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
            if (column.name.lower() == 'id'):
                did = column_util.data_type(column.datatype)
                break

        return did

IDENT = (' '*4)