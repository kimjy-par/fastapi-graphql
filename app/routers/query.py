import strawberry

from typing import List
from fastapi import Depends
from strawberry.types import Info
from app.schemas.user import User
from app.services.test_service import CustomContext

authors: List[str] = []



@strawberry.type
class Query:

    @strawberry.field(name="di_test")
    def di_test(self) -> User:
        #print((info.context.greeting))
        user = User(name="hello", age=100)
        return user
    @strawberry.field(name='fil')
    def all_authors(self) -> List[str]:
        return authors

    @strawberry.field(name='hello_world')
    def hello(self) -> str:
        return "hello GraphQL"

    @strawberry.field(name='user')
    def user(self) -> User:
        return User(name='patrick', age=100)
