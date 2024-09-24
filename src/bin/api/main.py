from fastapi import FastAPI
from app.routers import UserRouter, RoleRouter
from uvicorn import run

from app.infrastructure.bootstrap.runner import init_app
from app.infrastructure.config import RootConfig

from app.services import UserService, RoleService
from app.utils.ioc import ioc


def main():
    init_app(
        app_config_path="configs/app.yaml",
        database_config_path="configs/database.yaml",
        smtp_config_path="configs/smtp.yaml",
    )

    config = ioc.get(RootConfig)

    app = FastAPI(title='USER REST API', debug=config.app.debug)

    user_router = UserRouter(ioc.get(UserService))
    role_router = RoleRouter(ioc.get(RoleService))

    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(role_router, prefix='/role', tags=['role'])

    print(f"[📔] See docs on: http://{config.app.host}:{config.app.port}/docs")

    run(
        app,
        host=config.app.host,
        port=config.app.port,
    )


if __name__ == '__main__':
    main()
