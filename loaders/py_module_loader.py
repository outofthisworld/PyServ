"""PyModuleLoader"""
from importlib.util import spec_from_file_location, module_from_spec
from importlib.machinery import SourceFileLoader
from types import ModuleType
from .loader import Loader


class PyModuleLoader(Loader):
    """PyModuleLoader"""

    def _load(self, script_path: str, module_name: str) -> ModuleType:
        """Load"""
        if not script_path.endswith('.py'):
            raise ValueError("Invalid script path, must end with .py")

        spec = spec_from_file_location(
            module_name,
            loader=SourceFileLoader(module_name, script_path),
            location=script_path
        )
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
