import os
import config.sys

def get_plugin_base_dir():
    return os.path.join(sys.get_project_root(), 'plugins')

