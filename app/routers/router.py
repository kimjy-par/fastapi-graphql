import strawberry

from strawberry.fastapi import GraphQLRouter
from app.routers.query import Query
from app.routers.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

