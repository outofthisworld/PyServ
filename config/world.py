import os
from . import sys


def get_plugin_folder():
    """Get the plugin folder"""
    return 'plugins'

def get_plugin_base_dir():
    """Get plugin base directory"""
    return os.path.join(sys.get_project_root(), get_plugin_folder())
