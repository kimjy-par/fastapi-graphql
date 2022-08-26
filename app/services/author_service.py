from app.routers.query import authors

class AuthorService():
    def post(self, name: str) -> str:
        authors.append(name)
        return name
