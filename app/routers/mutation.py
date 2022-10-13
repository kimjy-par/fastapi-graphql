import strawberry

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from app.core.container import Container
from app.routers.query import authors
from app.services.author_service import AuthorService
from strawberry.types import Info
from strawberry.fastapi import BaseContext

class CustomContext(BaseContext):
    def __init__(self, greeting: str, name: str):
        self.greeting = greeting
        self.name = name

 
class MyClass():

    def __call__(self):
        print(self.custom_context_dependency())
        return self.custom_context_dependency()

    def custom_context_dependency(self) -> CustomContext:
        print("hello DI")
        return CustomContext(greeting='you rock!', name='John')

my_class = MyClass()

async def get_context(
    custom_context=Depends(my_class.custom_context_dependency)
):
    
    return custom_context

@strawberry.type
class Mutation():
 
    def __init__(
        self, service: AuthorService = Depends(Provide[Container.author_service])
    ) -> None:
        self.service = service

    @strawberry.field(name='add_author')
    def add_author(self, name: str) -> str:
        print(self)
        #authors.append(name)
        return name
    
    @strawberry.field(name='test_here')
    def example(self, name:str, info: Info
    ) -> str:
        return f"hello {name} {info.context.name}, {info.context.greeting}"

