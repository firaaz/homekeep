""" Organize the incoming files """

import os
import magic
from constants import TYPES


class Org(object):
    def __init__(self, config):
        self.config = config

    @staticmethod
    def to_folder(input_file):
        """ Get the folder that the file belongs to.
        Returns 'Undefined' if not one of the specified types, and then does
        not do anything.

        Args:
            input_file (str): file location of the file to be organized

        Result:
            String containing the location that the file needs to be moved to.
        """

        mime_val = magic.from_file(input_file, mime=True)
        mime = mime_val.split('/')[0]  # eg: 'audio'

        folder = TYPES.get(mime, 'undefined')

        return folder


    def organize_folder(self, folder_name):

        # Bottom up in case we use move, so that we can actually delete folders
        for root, _, files in os.walk(folder_name, topdown=False):
            for name in files:
                print(Org.to_folder(os.path.join(root, name)))
