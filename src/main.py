from fastapi import FastAPI

from src.settings import Settings
from src.app import get_router as get_app_router


def _include_routers(app: FastAPI, settings: Settings) -> None:
    routers_getters = (get_app_router,)

    for getter in routers_getters:
        router = getter(settings)
        app.include_router(router)


def get_app() -> FastAPI:
    app = FastAPI()
    settings = Settings()

    _include_routers(app, settings)

    return app
