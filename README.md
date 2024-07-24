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
[API]
host=127.0.0.1
port=8000

[DataBase]
type=mysql
host=127.0.0.1
port=3306
user=root
password=password
database=user_rest_api
```

2. Example for postgres

``` ini
[API]
host=127.0.0.1
port=8000

[DataBase]
type=mysql
host=127.0.0.1
port=5432
user=postgres
password=password
database=user_rest_api
```

3. Example for local (mysql)

``` ini
[API]
host=127.0.0.1
port=8000

[DataBase]
type=local
host=127.0.0.1
port=3306
user=root
password=password
database=user_rest_api
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