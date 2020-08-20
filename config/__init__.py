""" module for managing configurations

Priority to XDG values, if found they are used.
"""

import os
from ast import literal_eval
from dataclasses import dataclass
from configparser import ConfigParser


# NOTE: When adding new fields even add those to the _create_default
# and get_config_data functions
@dataclass
class Config:
    """ Config data """

    # meta configs
    config_path: str

    # Basic
    move: bool

    # Paths
    movie_directory: str
    tv_directory: str
    music_directory: str

    @classmethod
    def fromFile(cls):
        """ Create the Config object from the configuration file
        """

        config_path = Config.get_config_path()
        config_data = Config.get_config(config_path)

        return cls(**config_data)

    @staticmethod
    def get_config_path():
        """return config directory location

        Importance given to XDG values, if that exists we use that
        else we choose $HOME/.config

        Return:
            config_path (str): configuration directory location
        """
        if os.environ.get("XDG_CONFIG_HOME"):
            config_path = os.path.join(os.environ["XDG_CONFIG_HOME"], "homekeep.ini")
        else:
            config_path = os.path.join(os.environ["HOME"], ".config", "homekeep.ini")

        return config_path

    @staticmethod
    def get_config_data(config, config_path):
        """ config data extraction

        Args:
            config (ConfigParser): object that has the config file

        Result:
            dict of the config values
        """

        config_data = {
            'config_path': config_path,
            'move': literal_eval(config['basic']['move']),
            'movie_directory': config['paths']['movie_directory'],
            'tv_directory': config['paths']['tv_directory'],
            'music_directory': config['paths']['music_directory']
        }

        return config_data

    @staticmethod
    def get_config(config_path):
        """ Get ConfigParser Object

        Args:
            config_path (str): configuration directory location

        Return:
            ConfigParser object with config values

        """
        config = ConfigParser()

        # if file does not exist, create it before reading
        if not os.path.isfile(config_path):
            Config._create_default(config, config_path)

        config.read(config_path)
        config_data = Config.get_config_data(config, config_path)

        return config_data

    @staticmethod
    def _create_default(config, config_path):
        """ Default Values for configuration file """

        # Basic
        config.add_section("basic")
        config["basic"]["move"] = "False"

        # Paths
        config.add_section("paths")
        config["paths"]["movie_directory"] = os.path.join(os.environ["HOME"], "Videos", "Movies")
        config["paths"]["tv_directory"] = os.path.join(os.environ["HOME"], "Videos", "TV Shows")
        config["paths"]["music_directory"] = os.path.join(os.environ["HOME"], "Music")

        with open(config_path, "w") as file:
            config.write(file)
