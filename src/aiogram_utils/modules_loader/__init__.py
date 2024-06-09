import os
from importlib.machinery import SourceFileLoader
from pathlib import Path


class ModulesImporter():
    
    
    @staticmethod
    def import_path(path_to_search: str, modules_prefix: str) -> int:
        modules = Path(path_to_search).rglob("*.py")

        number = 0
        for module in modules:
            SourceFileLoader(f"{modules_prefix}_{number}", str(module)).load_module()
            number += 1

        return number
    