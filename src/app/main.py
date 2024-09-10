from fastapi import FastAPI
from routers import UserRouter, RoleRouter
from uvicorn import run

from data import AppConfig
from bootstrap.runner import init_app

from services import UserService, RoleService
from utils.ioc import ioc



if __name__ == '__main__':
    init_app()
    
    app = FastAPI(title='USER REST API', debug=True)

    user_router = UserRouter(ioc.get(UserService))
    role_router = RoleRouter(ioc.get(RoleService))

    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(role_router, prefix='/role', tags=['role'])


    run(
        app,
        host=AppConfig.host,
        port=AppConfig.port,
    )
