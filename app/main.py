from fastapi import FastAPI

from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from starlette.middleware.cors import CORSMiddleware
from app.routers.router import graphql_app
from app.core.container import Container

app = FastAPI()
app.container = Container()
app.include_router(graphql_app, prefix="/graphql")
