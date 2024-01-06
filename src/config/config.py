import os
from pathlib import Path

ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__))).parent
DATA_PATH = ROOT_PATH.parent / 'data'

# Validar se existe o arquivo tables.json
