import strawberry

from app.routers.query import authors

@strawberry.type
class Mutation():
    @strawberry.field
    def add_author(self, name: str) -> str:
        authors.append(name)
        return name
