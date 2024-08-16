from configparser import ConfigParser
import os


if 'config.ini' not in os.listdir('.'):
    raise ValueError('File config.ini not found.')

parser = ConfigParser()
parser.read(r'config.ini')


class DataBase:
    """
    ### Store the database settings

    @properties:
    1. type
    2. host
    3. port
    4. user
    5. pasword
    6. database
    """
    __section = 'DataBase'
    _avaiable_types = ['local', 'mysql', 'postgres']

    type = parser.get(__section, 'type')
    host = parser.get(__section, 'host')
    port = parser.getint(__section, 'port')
    user = parser.get(__section, 'user')
    password = parser.get(__section, 'password')
    database = parser.get(__section, 'database')

    # If type database is incorrect
    if type not in _avaiable_types:
        raise ValueError(f'database type must be {
                         _avaiable_types}, your value: {type}')

    # Create connection string for sqlite and other db types
    if type == 'local':
        db_path = f'database/'
        db_file = f'{database}.sqlite3'
        connection_string = f'sqlite://{db_path}{db_file}'
    else:
        if len(password) == 0:
            connection_string = f'{type}://{user}@{host}:{port}/{database}'
        else:
            connection_string = f'{
                type}://{user}:{password}@{host}:{port}/{database}'
