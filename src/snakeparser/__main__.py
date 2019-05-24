import argparse
import snakeparser

from snakeparser import __version__
from snakeparser import parse_to_yml


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('snakeparser')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    parser.add_argument('file', help='file or dir to parse')

    return parser

def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    parse_to_yml(args.file)


if __name__ == '__main__':
    main()