__all__ = ["get_parser"]

from configparser import ConfigParser
import os

def get_parser():
    parser = ConfigParser()
    parser.read(r'config.ini')

    if 'config.ini' not in os.listdir('.'):
        raise ValueError('File config.ini not found.')

    return parser
