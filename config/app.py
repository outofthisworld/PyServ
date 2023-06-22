from os import path
from .parser import parser

################################
# App vars
################################

ROOT_DIR = path.join(path.dirname(path.abspath(__file__)))
PLUGINS_DIR = path.join(ROOT_DIR, parser.get(
    'app', 'plugin_folder', fallback='plugins'))
