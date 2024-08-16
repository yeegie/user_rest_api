from configparser import ConfigParser
import os


if 'config.ini' not in os.listdir('.'):
    raise ValueError('File config.ini not found.')

parser = ConfigParser()
parser.read(r'config.ini')


class API:
    section = 'API'
    host = parser.get(section, 'host')
    port = parser.getint(section, 'port')


class DataBase:
    section = 'DataBase'
    _avaiable_types = ['local', 'mysql', 'postgres']

    type = parser.get(section, 'type')
    host = parser.get(section, 'host')
    port = parser.getint(section, 'port')
    user = parser.get(section, 'user')
    password = parser.get(section, 'password')
    database = parser.get(section, 'database')

    # If type database is incorrect
    if type not in _avaiable_types:
        raise ValueError(f'database type must be {_avaiable_types}, your value: {type}')
    
    # Create connection string for sqlite and other db types
    if type == 'local':
        db_path = f'database/'
        db_file = f'{database}.sqlite3'
        connection_string = f'sqlite://{db_path}{db_file}'
    else:
        if len(password) == 0:
            connection_string = f'{type}://{user}@{host}:{port}/{database}'
        else:
            connection_string = f'{type}://{user}:{password}@{host}:{port}/{database}'

