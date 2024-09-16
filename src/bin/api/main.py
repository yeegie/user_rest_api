from fastapi import FastAPI
from app.routers import UserRouter, RoleRouter
from uvicorn import run

from app.bootstrap.runner import init_app

from app.services import UserService, RoleService
from app.utils.ioc import ioc


def main():
    init_app(
        config_path="../config.ini"
    )

    app = FastAPI(title='USER REST API', debug=True)

    user_router = UserRouter(ioc.get(UserService))
    role_router = RoleRouter(ioc.get(RoleService))

    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(role_router, prefix='/role', tags=['role'])

    run(
        app,
        host="localhost",
        port="8000",
    )


if __name__ == '__main__':
    main()
