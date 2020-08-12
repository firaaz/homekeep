""" Entry point for the script """

from argparse import ArgumentParser

from config import Config

if __name__ == '__main__':
    parser = ArgumentParser("Organize files in a directory.")
    parser.add_argument("directory", metavar="dir", type=str,
                        help="Directory to organize")
    args = parser.parse_args()
    config = Config()

    if args.directory:
        target_dir = args.directory
        print(target_dir)
