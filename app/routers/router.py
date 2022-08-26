import strawberry

from strawberry.fastapi import GraphQLRouter
from app.routers.query import Query
from app.routers.mutation import Mutation

query = Query()
mutation = Mutation()
print('mutation??', dir(mutation))
schema = strawberry.Schema(query=query, mutation=mutation)
graphql_app = GraphQLRouter(schema)

