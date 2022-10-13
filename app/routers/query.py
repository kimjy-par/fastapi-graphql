import strawberry

from typing import List
from fastapi import Depends
from strawberry.types import Info
from app.schemas.user import User

authors: List[str] = []

def custom_context_dependency() -> str:
    return "John"

async def get_context(
    custom_value = Depends(custom_context_dependency)
):
    return{
        "custom_value": custom_value,
    }


@strawberry.type
class Query:

    @strawberry.field(name="di_test")
    def di_test(self, info: Info) -> str:
        return f"hello {info.context['custom_value']}"
    @strawberry.field(name='fil')
    def all_authors(self) -> List[str]:
        return authors

    @strawberry.field(name='hello_world')
    def hello(self) -> str:
        return "hello GraphQL"

    @strawberry.field(name='user')
    def user(self) -> User:
        return User(name='patrick', age=100)
