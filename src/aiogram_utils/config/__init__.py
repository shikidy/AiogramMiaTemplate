import os
from typing import Dict

import toml


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=Singleton):


    def __init__(self) -> None:
        self.__data: Dict = {}
        config_path = "config.toml"

        if not os.path.exists(config_path):
            raise ValueError("Thres is no config.toml V_V")
        
        self.__load_config(config_path)

    
    def __load_config(self, path: str):
        """Loading config from path

        :params path: path to config.toml
        """
        with open(path) as f:
            self.__data = toml.load(f)
            self.__data =  {k.lower(): v for k, v in self.__data.items()}

    def __getattr__(self, name: str):
        data = self.__data.get(name.lower())
        if not data:
            raise AttributeError(f"There is no {name} in config.toml")
        return data
        
