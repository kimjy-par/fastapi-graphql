from fastapi import FastAPI

from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from starlette.middleware.cors import CORSMiddleware
from app.routers.router import graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
