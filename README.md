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
repository_type=database
host=127.0.0.1
port=8000
debug=True

[DataBase]
db_type=mysql
host=127.0.0.1
port=3306
user=root
password=password
database=database
```

2. Example for postgres

``` ini
[Application]
repository_type=database
host=127.0.0.1
port=8000
debug=True

[DataBase]
db_type=postgres
host=127.0.0.1
port=5432
user=postgres
password=password
database=database
```

3. Example for memory

``` ini
[Application]
repository_type=memory
host=127.0.0.1
port=8000
debug=True

[DataBase]
db_type=any
host=any
port=1111
user=any
password=any
database=any
```

4. Example for redis

``` ini
[Application]
repository_type=redis
host=127.0.0.1
port=8000
debug=True

[DataBase]
db_type=any
host=127.0.0.1
port=6379
user=any
password=any
database=database
```

<hr>

#### Run application


``` bash
pip install -e .
user_rest_api
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