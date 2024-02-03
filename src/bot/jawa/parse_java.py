from parser.parser_base import ParserBase
from pathlib import Path


class ParseJava(ParserBase):

    def execute(self, config):

        super().execute(config)

        # variaveis personalizaveis
        self.var_template['path_class_exception_nocontent'] = 'share.exception'
        self.var_template['class_name_exception_nocontent'] = 'NoContentException'

        self.var_template['path_class_exception_business'] = 'share.exception'
        self.var_template['class_name_exception_business'] = 'BusinessException'

        #variaveis conforme o template.yaml
        self.__preecher_var__(self.table.name)
        self.var_template['body'] = self.__body_columns__()
        self.var_template['body_jpa'] = self.__body_jpa__()

        self.var_template['package_path'] = self.package_path
        self.var_template['package_artefato'] = self.package_path
        self.var_template['datatype_id'] = self.__datatype_id__()

        self.var_template['table_name'] = self.table.name
        self.var_template['table_name_lower'] = self.table.name.lower()

        self.var_template['import_header'] = self.__import_header__(self.var_template['body'])        

        for r in self.templates:
            path = Path(r.path)
            path_class = r.path.replace('/', '.')
            # print(r.name)

            self.var_template['class_name'] = r.get_class_name(self.table.name)
            self.var_template['path_class'] = path_class
            self.var_template['mapper_ignore_id'] = ''

            template = self.parse_template(r.name)
            self.file_create(path / r.get_file_name(self.table.name), template)
            # print(r.name)

    def __preecher_var__(self, table_name):

        for r in self.templates:
            key = r.key.replace('-', '_')
            path_class = f'path_class_{key}'
            class_name = f'class_name_{key}'
            self.var_template[path_class] = r.path.replace('/', '.')
            self.var_template[class_name] = r.get_class_name(table_name)

    def __import_header__(self,body):
        result = ""
        if "private LocalDateTime" in body:
            result += "\nimport java.time.LocalDateTime;"
        return result
