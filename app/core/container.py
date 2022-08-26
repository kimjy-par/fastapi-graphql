from dependency_injector import containers, providers
from app.services.author_service import AuthorService
from app.routers.query import authors

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.routers.mutation',
        ]
    )

    author_service = providers.Factory(AuthorService)
