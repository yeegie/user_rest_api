from data import AppConfig
from runner import init_app
from uvicorn import run


if __name__ == '__main__':
    app = init_app()

    run(
        app,
        host=AppConfig.host,
        port=AppConfig.port,
    )
