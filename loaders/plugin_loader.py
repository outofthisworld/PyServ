"""
    PluginLoader
"""
import os
from . import Loader, ModuleLoader


class PluginLoader(Loader):
    """
        PluginLoader
    """

    def __init__(self):
        self._module_loader: ModuleLoader = ModuleLoader()

    def load(self, *args, **kwargs):
        (plugin_dir) = args
        return [self._module_loader.load(plugin_dir, file[:-3]) for file in os.listdir(plugin_dir) if file.endswith('.py')]