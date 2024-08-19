from configparser import ConfigParser
from .config_parser import get_parser


class AppConfig:
    """
    ### Store the app settings

    @properties:
    1. host: str - look like this: "localhost" or "127.0.0.1"
    2. port: int
    """

    def __init__(self, parser: ConfigParser) -> None:
        self.__section = "Application"
        self.__parser = parser

        self.host = parser.get(self.__section, 'host')
        self.port = parser.getint(self.__section, 'port')


app_config = AppConfig(parser=get_parser())
