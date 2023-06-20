"""
    PluginLoader
"""
import os
import types
import typing
from . import Loader, ModuleLoader
from events import EventEmitter

class PluginLoader(Loader):
    """
        PluginLoader
    """

    def __init__(self):
        self._module_loader: ModuleLoader = ModuleLoader()
        self._plugins: typing.List[types.ModuleType] = []
        self._event_emitter: EventEmitter = EventEmitter()

    def load(self, *args, **kwargs) -> typing.List[types.ModuleType]:
        """
            Loads plugins
        """
        (plugin_dir,) = args
        self._plugins += [self._module_loader.load(
            plugin_dir, file[:-3]) for file in os.listdir(plugin_dir) if file.endswith('.py') and not file.startswith('__init__')]
        self._event_emitter.emit('loaded', self._plugins)
        return self._plugins

    @property
    def plugins(self) -> typing.List[types.ModuleType]:
        """
            Return the loaded plugins
        """
        return self._plugins
