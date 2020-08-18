#!/bin/env python3
""" Entry point for the script """

from argparse import ArgumentParser

from config import Config
from handler import Handler


def main():
    """ Main control flow of the program """

    parser = ArgumentParser("Organize files in a directory.")
    parser.add_argument("directory", metavar="dir", type=str,
                        help="Directory to organize")
    args = parser.parse_args()
    config = Config()
    handler = Handler()

    if args.directory:
        target_dir = args.directory
        handler.handle(target_dir)


if __name__ == '__main__':
    main()
