from strawberry.fastapi import BaseContext
class Model():
    def __init__(self):
        self.hello="hello"

    def inference(self):
        print(self.hello, "inference")

model = Model()
class CustomContext(BaseContext):
    def __init__(self, greeting: str, name: str,
                 model: Model=model
    ):
        self.greeting = greeting
        self.name = name
        self.model = model
 
class MyClass():

    def __call__(self):
        print(self.custom_context_dependency())
        return self.custom_context_dependency()

    def custom_context_dependency(self) -> CustomContext:
        custom_context = CustomContext(greeting='you rock!', name='John', model=model)
        custom_context.model.inference()
        return custom_context

my_class = MyClass()
