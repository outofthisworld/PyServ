"""App config"""
from os import path
from . import config

ROOT_DIR = path.join(path.dirname(path.abspath(__file__)))
PLUGINS_DIR = path.join(ROOT_DIR, config.get(
    'app', 'plugins_folder', fallback='plugins'))
