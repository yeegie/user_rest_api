## Instalation and running
1. Create virtual environment.
``` python
python -m venv venv
```
<br>
2. Activate virtual environment.

Linux:
``` bash
source ./venv/bin/activate
```

Windows:
``` bash
source .\venv\Scripts\activate
```
<br>
3. Install dependencies.

``` bash
pip install -r requirements.txt
```
<br>
4. Create a config.ini file in the root directory of the project and fill it according to the example conifg_example.txt according to your requirements.
<hr>

#### Below are examples of config.ini for different databases
___Before use, create a database called - user_rest_api___

1. Example for mysql

``` ini
[Application]
host=127.0.0.1
port=8000

[DataBase]
db_type=database
db_uri=mysql://root:password@localhost:3306/database
```

2. Example for postgres

``` ini
[Application]
host=127.0.0.1
port=8000

[DataBase]
db_type=database
db_uri=postgres://postgres:password@localhost:5432/database
```

3. Example for local (sqlite3)

``` ini
[Application]
host=127.0.0.1
port=8000

[DataBase]
db_type=database
db_type=sqlite://:memory:
```

4. Example for redis

``` ini
[Application]
host=127.0.0.1
port=8000

[DataBase]
db_type=redis
db_type=redis://localhost:6379
```

4. Example for memory

``` ini
[Application]
host=127.0.0.1
port=8000

[DataBase]
db_type=memory
db_type=none
```
<hr>

#### Run application
``` bash
python main.py
```

Example of successful launch of the application:
``` bash
❯ python main.py
INFO:     Started server process [34967]
INFO:     Waiting for application startup.
INFO:__main__:[⭐] Starting app...
INFO:database:[📦] Database(local) connected...
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```