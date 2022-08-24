import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from starlette.middleware.cors import CORSMiddleware

authors: list[str] = []

@strawberry.type
class User:
    name: str
    age: int

@strawberry.type
class Query():
    @strawberry.field
    def all_authors(self) -> list[str]:
        return authors

    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def user(self) -> User:
        return User(name='patrick', age=100)

@strawberry.type
class Mutation():
    @strawberry.field
    def add_author(self, name: str) -> str:
        authors.append(name)
        return name

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
@app.get('/')
def read_root():
    return 'hello FastAPI & GraphQL'

app.include_router(graphql_app, prefix="/graphql")
