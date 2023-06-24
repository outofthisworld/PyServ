"""App config"""
from os import path
from . import ROOT_DIR, config


PLUGINS_DIR = path.join(ROOT_DIR, config.get(
    'app', 'plugins_folder', fallback='plugins'))
