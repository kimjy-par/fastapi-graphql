from dependency_injector import containers, providers
from fastapi import Depends
from strawberry.fastapi import BaseContext

from app.models.model import Model

model = Model()

class CustomContext(BaseContext):
    def __init__(self, greeting: str, name: str,
                 model: Model=model
    ):
        self.greeting = greeting
        self.name = name
        self.model = model

def custom_context():
    return CustomContext(greeting='hello', name='jacob')

async def context_container(
    custom_context=Depends(custom_context)
):
    custom_context
    return custom_context

