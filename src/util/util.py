import re
import sys



def camelCase(s):
    words = s.split('_')
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def extrair_numeros(value, value_default=None):
    numeros = re.sub(r'\D', '', value)
    if numeros:
        return int(numeros)
    else:
        return value_default


def if_error_exit(flag_exit: bool, msg_erro):
    if flag_exit:
        print(msg_erro)
        sys.exit()


def if_isnone_exit(value: bool, msg_erro):
    if value is None:
        print(msg_erro)
        sys.exit()


def FILE_NOTFOUND(m): return f"O arquivo '{m}' não foi encontrado."


def if_file_not_exists_exit(file):
    if_error_exit(not file.exists(), FILE_NOTFOUND(file))
