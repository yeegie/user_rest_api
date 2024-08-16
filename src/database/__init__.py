from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError
from data.config import DataBase

import os
import logging
import time

logger = logging.getLogger(__name__)


async def init_database():
    # Check database.sqlite3 file
    if DataBase.type == 'local':
        db_file_exist = DataBase.db_file in os.listdir(DataBase.db_path)

        # If db file not exist - create
        db_path = DataBase.db_path
        db_file = DataBase.db_file

        if db_file_exist is False:
            with open(db_path + db_file, 'a'):
                os.utime(db_path + db_file, None)
            logger.info(f'[!] Database created {db_path + db_file}')

    time.sleep(3)

    try:
        await Tortoise.init(
            db_url=DataBase.connection_string,
            modules={'models': ['database.models']},
        )

        await Tortoise.generate_schemas()
        logger.info(f'[📦] Database({DataBase.type}) connected...')
    except DBConnectionError as ex:
        logger.critical(f'Data base connection error to {DataBase.connection_string}')
    except Exception as ex:
        logger.critical(f'DATABASE CONNECTION ERROR: {str(ex)}. {DataBase.connection_string}')


async def close_database():
    await Tortoise.close_connections()
