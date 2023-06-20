"""
    ModuleLoader
"""
from types import ModuleType
import importlib.util
from . import Loader
import os


class PyScriptLoader(importlib.machinery.SourceFileLoader):
    def __init__(self, module_name, module_path):
        super().__init__(module_name, module_path)


class PyModuleLoader(Loader):
    """
        ModuleLoader
    """
    async def _load(self, script_path: str, module_name: str) -> ModuleType:
        spec = importlib.util.spec_from_file_location(
            module_name,
            loader=PyScriptLoader(module_name, script_path),
            location=script_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
