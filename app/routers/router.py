import strawberry

from strawberry.fastapi import GraphQLRouter
from app.services.query import Query
from app.services.mutation import Mutation
from app.core.container import context_container

query = Query()
mutation = Mutation()
strawberry_config = strawberry.schema.config.StrawberryConfig(auto_camel_case=False)
schema = strawberry.Schema(query=query, mutation=mutation, config=strawberry_config)
graphql_app = GraphQLRouter(schema, context_getter=context_container)

