import types
import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from starlette.middleware.cors import CORSMiddleware
from app.schemas.user import User
from app.routers.query import Query
from app.routers.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")
