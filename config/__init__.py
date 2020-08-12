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
    """return config directory location

    Importance given to XDG values, if that exists we use that
    else we choose $HOME/.config

    Return:
    config_path (str): configuration directory location
    """
    if os.environ.get("XDG_CONFIG_HOME"):
        config_path = os.path.join(os.environ["XDG_CONFIG_HOME"], "homekeep.ini")
    config_path = os.path.join(os.environ["HOME"], ".config", "homekeep.ini")

    return config_path


def get_config(config_path):
    """ Get Config Parser Object

    Args:
        config_path (str): configuration directory location

    Return:
        ConfigParser object with config values

    """
    config = ConfigParser()

    if not os.path.isfile(config_path):
        create_default_config(config, config_path)

    config.read(config_path)

    return config


def create_default_config(config, config_path):
    """ Default Values for configuration file """

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
