import os
import logging

from .config import Config
from .modules_loader import ModulesImporter
from .loader import bot, dp


logger = logging.getLogger(__name__)


def import_project():
    
    base_path = "src/bot_src/"
    to_import = {
        "middleware": "middlewares",
        "filter": "filters",
        "handler": "handlers"
    }
    
    for key in to_import.keys():

        count = ModulesImporter.import_path(os.path.join(base_path, to_import.get(key)), key)
        logger.debug(f"Imported {count} modules with handlers")
