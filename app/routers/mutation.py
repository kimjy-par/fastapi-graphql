import strawberry

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from app.core.container import Container
from app.routers.query import authors
from app.services.author_service import AuthorService

@strawberry.type
class Mutation():
    @inject
    def __init__(self,
        service: AuthorService = Depends(Provide[Container.author_service])
    ):
        self.service=service

    @strawberry.field
    def add_author(self, name: str) -> str:
        print('!!test here', dir(self))
        self.service.post(name)
        #authors.append(name)
        return name

router = APIRouter()
@router.get('/')
@inject
async def test_func(
    service: AuthorService = Depends(Provide[Container.author_service])
)-> str:
    service.post('hello dependency injection')
    return 'hello'
