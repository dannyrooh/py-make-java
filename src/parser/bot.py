import importlib


class Bot():
    def __init__(self, config):
        self.config = config

    def execute(self, templates, path_destiny, table, datatypes):
        # Nome do módulo e nome da classe
        # modulo_nome = "bot.jawa.parse_java"
        # classe_nome = "ParseJava"

        module_name = self.config['module']
        classe_name = self.config['classe']

        # Importa o módulo dinamicamente
        modulo = importlib.import_module(module_name)

        # Obtém a classe do módulo
        classe = getattr(modulo, classe_name)

        # Cria uma instância da classe
        instancia = classe()

        # Chama o método execute da instância
        config = {}
        config['datatypes'] = datatypes
        config['templates'] = templates
        config['table'] = table
        config['path_destiny'] = path_destiny
        config['package_path'] = 'br.com.klabin.florestal.matrizinsumos.lookup'
        instancia.execute(config)
