import strawberry

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from app.services.query import authors
from strawberry.types import Info
from strawberry.fastapi import BaseContext

@strawberry.type
class Mutation():

    @strawberry.field(name='add_author')
    def add_author(self, name: str) -> str:
        print(self)
        authors.append(name)
        return name
    
    @strawberry.field(name='test_here')
    def example(self, name:str, info: Info
    ) -> str:
        return info
