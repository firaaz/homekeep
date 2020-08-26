""" Organize the incoming files
Respect config values, whereever appropriate
"""

import os
import shutil
import magic
from constants import FOLDERS


class Org:
    """ Organizer object"""
    def __init__(self, config):
        self.config = config

    def to_folder(self, input_file):
        """ Get the folder that the file belongs to.
        Returns 'Undefined' if not one of the specified types, and then does
        not do anything.

        Args:
            input_file (str): file location of the file to be organized

        Result:
            String containing the location that the file needs to be moved to.
        """

        mime_val = magic.from_file(input_file, mime=True)
        mime = mime_val.split('/')[0]

        folder = FOLDERS.get(mime)
        # to_location = getattr(self.config, folder)

        # TODO: Make it work for seperating movies and tv shows
        return getattr(self.config, folder) if folder else None

    def organize_directory(self, folder_name):
        """ Organize the files in a directory"""

        # Bottom up in case we use move, so that we can actually delete folders
        for root, _, files in os.walk(folder_name, topdown=False):
            for name in files:
                current_file = os.path.join(root, name)
                to_location = self.to_folder(current_file)
                if not to_location:
                    continue
                to_location = to_location + '/' + name
                self.move(current_file, to_location)

    def move(self, current_file, to_location):
        """ Move the file to the given folder 
        Args:
            current_file (str): source file location
            to_location (str): destination file location

        Result:
            None
        """
        if self.config.move:
            shutil.move(current_file, to_location)
        else:
            shutil.copyfile(current_file, to_location)