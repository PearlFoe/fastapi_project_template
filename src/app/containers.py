from dependency_injector import containers, providers


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.app.routers",
        ],
    )
    env = providers.Configuration()
