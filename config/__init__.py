""" module for managing configurations """

import os
from dataclasses import dataclass
from configparser import ConfigParser


@dataclass
class Config:
    config_path: str

    def __init__(self):
        self.config_path = get_config_path()
        self.config = set_config(config_path)


def get_config_path():
    if (os.environ.get("XDG_CONFIG_HOME"):
        return os.path.join(os.environ["XDG_CONFIG_HOME"], "homekeep.ini")
    return os.path.join(os.environ["HOME"], ".config", "homekeep.ini")

def set_config(config_path):
    config = ConfigParser()
