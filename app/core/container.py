from dependency_injector import containers, providers
from fastapi import Depends

from app.services.test_service import my_class
from app.routers.query import authors

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.routers.mutation',
        ]
    )


async def get_context(
    custom_context=Depends(my_class.custom_context_dependency)
):
    return custom_context

