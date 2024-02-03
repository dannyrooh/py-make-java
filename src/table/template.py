from util.file_util import file_yaml
from pathlib import Path


class TemplateRow:
    def __init__(self, name, prefix, sufix, path, key, fix=None, ext='.java') -> None:
        self.name = name
        self.prefix = prefix
        self.sufix = sufix
        self.fix = fix
        self.path = path
        self.key = key
        self.ext = ext

    # retorna o nome do template
    def get_class_name(self, table_name):
        prefix = '' if self.prefix is None else self.prefix
        sufix = '' if self.sufix is None else self.sufix
        table_name = '' if self.fix else table_name
        return f'{prefix}{table_name}{sufix}'

    def get_file_name(self, table_name):
        ext = '' if self.ext is None else self.ext
        return f'{self.get_class_name(table_name)}{ext}'


class Template:
    def __init__(self, cfg) -> None:
        self.cfg = cfg

        self.rows = []

    def __path_template__(self, name_template):
        return Path(self.cfg['template']['dir']) / name_template

    def execute(self):

        data = file_yaml(self.cfg['template']['name'])

        self.__folders__(data['root'])

        return self.rows

    def __folders__(self, no):

        # if_error_exit(not isinstance(no, dict), 'Erro ao informar a pasta ')
        if isinstance(no, dict):
            for k, v in no.items():
                if k == 'folders':
                    # print(type(k))
                    for i in range(len(v)):
                        # print(i,type(v[i]))
                        if isinstance(v[i], dict):
                            for kk, vv in v[i].items():
                                # print(kk, type(vv))
                                if kk == 'folder':
                                    if isinstance(vv, dict):
                                        for kkk, vvv in vv.items():
                                            if kkk == 'folders':
                                                self.__folders__(vvv)
        elif isinstance(no, list):
            for i in range(len(no)):
                # print(type(no[i]))
                if isinstance(no[i], dict):
                    for k, v in no[i].items():
                        # print(k, type(v))
                        if k == 'folder':
                            if isinstance(v, dict):
                                for k1, v1 in v.items():
                                    # print(k1, type(v1))
                                    if k1 == 'name':
                                        # folder += f(v1)
                                        # print(v1)
                                        # folder += f(v1)
                                        pass

                                    if k1 == 'files':
                                        # print('files', type(v1))
                                        for j in range(len(v1)):
                                            # print(type(v1[j]))
                                            for k2, v2 in v1[j].items():
                                                self.rows.append(TemplateRow(
                                                    self.__path_template__(
                                                        v2['template']),
                                                    v2['prefix'],
                                                    v2['sufix'],
                                                    v2['path'],
                                                    v2['key'],
                                                    v2.get('fix', None)))

                                    if k1 == 'folders':
                                        # print(folder, type(v1), k)
                                        self.__folders__(v1)
