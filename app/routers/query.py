import strawberry

from app.schemas.user import User

authors: list[str] = []

@strawberry.type
class Query:
    @strawberry.field(name='fil')
    def all_authors(self) -> list[str]:
        return authors

    @strawberry.field
    def hello(self) -> str:
        return "hello world"

    @strawberry.field
    def user(self) -> User:
        return User(name='patrick', age=100)
