import strawberry

from strawberry.fastapi import GraphQLRouter
from app.routers.query import Query
from app.routers.mutation import Mutation, get_context

query = Query()
mutation = Mutation()
schema = strawberry.Schema(query=query, mutation=mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)

