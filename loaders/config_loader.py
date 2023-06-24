"""ConfigLoader"""
from configparser import ConfigParser
from .loader import Loader

class ConfigLoader(Loader):
    """ConfigLoader"""

    def _load(self, *args, **kwargs) -> ConfigParser:
        """Load"""
        config = ConfigParser()
        path, = args
        config.read(path)
        return config
