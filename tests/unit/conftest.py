import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from dependency_injector.containers import DeclarativeContainer

from src.main import get_app
from src.settings import Settings

from src.app.containers import AppContainer


@pytest.fixture(scope="session")
def app():
    return get_app()


@pytest.fixture(scope="class")
def containers(
    app_container: AppContainer,
):
    return (app_container,)


@pytest.fixture(scope="class")
def client(app: FastAPI, containers: tuple[DeclarativeContainer]):
    return TestClient(app)


@pytest.fixture(scope="class")
def settings():
    return Settings()


@pytest.fixture(scope="class")
def app_container(
    settings: Settings,
):
    container = AppContainer()
    container.env.from_dict(settings.model_dump())
    return container
