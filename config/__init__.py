"""config"""
from loaders import ConfigLoader

from .app import *
from .server import *
from .world import *

config = ConfigLoader().load()
