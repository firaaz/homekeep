""" module for managing configurations """

import os
from ast import literal_eval
from dataclasses import dataclass
from configparser import ConfigParser


@dataclass
class Config:
    
    config_path: str

    # Basic
    move: bool

    # Paths
    movie_directory = str
    tv_show_directory = str
    music_directory = str

    def __init__(self):
        self.config_path = get_config_path()
        config = get_config(self.config_path)

        self.move = literal_eval(config["Basic"]["Move"])

        self.movie_directory = config["Paths"]["MoviesDirectory"]
        self.tv_show_directory = config["Paths"]["TvShowsDirectory"]
        self.music_directory = config["Paths"]["MusicDirectory"]


def get_config_path():
    if os.environ.get("XDG_CONFIG_HOME"):
        return os.path.join(os.environ["XDG_CONFIG_HOME"], "homekeep.ini")
    return os.path.join(os.environ["HOME"], ".config", "homekeep.ini")


def get_config(config_path):
    config = ConfigParser()

    if os.path.isfile(config_path):
        config.read(config_path)
        return config

    # Basic
    config.add_section("Basic")
    config["Basic"]["Move"] = "False"

    # Paths
    config.add_section("Paths")
    config["Paths"]["MoviesDirectory"] = os.path.join(os.environ["HOME"], "Movies")
    config["Paths"]["TvShowsDirectory"] = os.path.join(os.environ["HOME"], "TV Shows")
    config["Paths"]["MusicDirectory"] = os.path.join(os.environ["HOME"], "Music")

    with open(config_path, "w") as file:
        config.write(file)
        
    return config
