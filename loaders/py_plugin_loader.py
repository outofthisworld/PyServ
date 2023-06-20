"""
    PluginLoader
"""
import os
import types
import typing
from . import Loader, PyModuleLoader
from events import EventEmitter


PY_FILE_EXTENSION = '.py'
PY_INIT_FILE = '__init__'

class PluginLoader(Loader):
    """
        PluginLoader
    """

    def __init__(self):
        super().__init__()
        self._module_loader: PyModuleLoader = PyModuleLoader()
        self._plugins: typing.List[types.ModuleType] = []

    async def _load(self, *args, **kwargs) -> typing.List[types.ModuleType]:
        """
            Loads plugins
        """
        plugin_dir, = args
        self._plugins.extend(await self._module_loader.load(
            os.path.join(plugin_dir, file), file[:-len(PY_FILE_EXTENSION)]) 
            for file in os.listdir(plugin_dir) 
            if file.endswith(PY_FILE_EXTENSION) and not file.startswith(PY_INIT_FILE)
        )
        return self._plugins

    @property
    def plugins(self) -> typing.List[types.ModuleType]:
        """
            Return the loaded plugins
        """
        return self._plugins
