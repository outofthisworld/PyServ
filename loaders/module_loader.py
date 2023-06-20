"""
    ModuleLoader
"""
from types import ModuleType
import importlib.util
from . import Loader


class PyScriptLoader(importlib.machinery.ExtensionFileLoader):
    def create_module(self, spec):
        return ModuleType(spec.name)

class ModuleLoader(Loader):
    """
        ModuleLoader
    """
    def load(self, *args, **kwargs) -> ModuleType:
        (module_path, module_name) = args
        loader = PyScriptLoader(module_name, module_path)
        spec = importlib.util.spec_from_file_location(module_name, loader=loader, submodule_search_locations=[module_path])
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
