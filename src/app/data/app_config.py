from configparser import ConfigParser
import os


if 'config.ini' not in os.listdir('.'):
    raise ValueError('File config.ini not found.')

parser = ConfigParser()
parser.read(r'config.ini')


class API:
    """
    ### Store the app settings
    
    @properties:
    1. host: str - look like this: "localhost" or "127.0.0.1"
    2. port: int
    """
    __section = 'API'
    host = parser.get(__section, 'host')
    port = parser.getint(__section, 'port')
