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
        self._plugins = []

    def load(self, *args, **kwargs):
        """
            Loads plugins
        """
        (plugin_dir) = args
        self._plugins += [self._module_loader.load(
            plugin_dir, file[:-3]) for file in os.listdir(plugin_dir) if file.endswith('.py')]
        for module in self._plugins:
            if callable(module.boot) and not module.plugin_init:
                module.boot()
                module.plugin_init = True

    @property
    def plugins(self):
        """
            Return the loaded plugins
        """
        return self._plugins
