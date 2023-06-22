"""ConfigLoader"""
from os import path
from configparser import ConfigParser
from config.app import ROOT_DIR
from . import Loader

class ConfigLoader(Loader):
    """ConfigLoader"""

    def _load(self, *args, **kwargs) -> ConfigParser:
        """Load"""
        config = ConfigParser()

        config.read(path.join(ROOT_DIR, 'config', 'config.ini'))
        return config
