"""config"""
from os import path
from loaders import ConfigLoader

ROOT_DIR = path.join(path.dirname(path.abspath(__file__)))

config = ConfigLoader().load(path.join(ROOT_DIR, 'config', 'config.ini'))

from .app import *
from .server import *
from .world import *
