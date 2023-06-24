"""Plugin loader for python plugins"""
from os import listdir, path
from types import ModuleType
from typing import List
from .sequence_loader import SequenceLoader
from .py_module_loader import PyModuleLoader


PY_FILE_EXTENSION = '.py'
PY_INIT_FILE = '__init__'


class PyPluginLoader(SequenceLoader):
    """Plugin Loader"""

    def __init__(self):
        """Init"""
        super().__init__()
        self._module_loader: PyModuleLoader = PyModuleLoader()
        self._data: List[ModuleType] = []

    def _load(self, *args, **kwargs) -> List[ModuleType]:
        """Load plugins"""
        plugin_dir, = args
        self._data.extend(self._module_loader.load(
            path.join(plugin_dir, file), file[:-len(PY_FILE_EXTENSION)])
            for file in listdir(plugin_dir)
            if file.endswith(PY_FILE_EXTENSION) and not file.startswith(PY_INIT_FILE)
        )
        return self._data

    def boot(self, *args, **kwargs):
        """Boot Modules"""
        for module in self:
            if hasattr(module, 'boot') and callable(module.boot):
                module.boot(*args, **kwargs)

    async def boot_async(self, *args, **kwargs):
        """Boot Modules Async"""
        return self.boot(*args, **kwargs)

    @property
    def plugins(self) -> List[ModuleType]:
        """Plugins"""
        return self._data
