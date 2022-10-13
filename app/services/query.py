import json
import strawberry

from typing import List
from strawberry.types import Info
from app.schemas.user import User
from app.schemas.inference_result import InferenceResult
authors: List[str] = []

@strawberry.type
class Query:

    @strawberry.field(name='inference')
    def inference(self, image_url: str, info: Info) -> InferenceResult:
        info.context.model.inference()

        inference_result = InferenceResult(
            data={
                'image_url':image_url,
                'result':[1,1,1,2,2]
            }
        )
        return inference_result

    @strawberry.field(name="di_test")
    def di_test(self, info: Info) -> User:
        info.context.model.inference()
        user = User(name="hello", age=100)
        return user

    @strawberry.field(name='fil')
    def all_authors(self) -> List[str]:
        return authors

    @strawberry.field(name='hello_world',metadata={'image_url':'image_url'})
    def hello(self, info: Info) -> str:        
        return 'hello graphql'

    @strawberry.field(name='user')
    def user(self) -> User:
        return User(name='patrick', age=100)