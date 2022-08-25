import strawberry.type

@strawberry.type
class Query:
    @strawberry.field
    def all_authors(self) -> list[str]:
