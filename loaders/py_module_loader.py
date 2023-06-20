"""
    ModuleLoader
"""
import os
import importlib.util
from types import ModuleType
from importlib.machinery import SourceFileLoader
from . import Loader

class PyModuleLoader(Loader):
    """
        ModuleLoader
    """
    async def _load(self, script_path: str, module_name: str) -> ModuleType:
        if not script_path.endswith('.py'):
            raise ValueError("Invalid script path, must end with .py")
        
        spec = importlib.util.spec_from_file_location(
            module_name,
            loader=SourceFileLoader(module_name, script_path),
            location=script_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
