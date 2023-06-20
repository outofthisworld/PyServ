"""
    ModuleLoader
"""
from types import ModuleType
import importlib.util
from . import Loader


class ModuleLoader(Loader):
    """
        ModuleLoader
    """

    def load(self, *args, **kwargs) -> ModuleType:
        (module_path, module_name) = args
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
