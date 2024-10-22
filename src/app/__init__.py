from fastapi import APIRouter

from src.settings import Settings
from .containers import AppContainer
from .routers import router


def _get_container(settings: Settings) -> AppContainer:
    container = AppContainer()
    container.env.from_dict(settings.model_dump())
    return container


def get_router(settings: Settings) -> APIRouter:
    _router = APIRouter(prefix="")
    _router.container = _get_container(settings)
    _router.include_router(router)
    return _router
