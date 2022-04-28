import imp
from starlette.applications import  Starlette
from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route

class HomePage(HTTPEndpoint): 
    async def get(self, request): 
        return PlainTextResponse("Sample this is a End Point")


class User(HTTPEndpoint):
    async def get(self, request):
        name = request.path_params['username']
        return PlainTextResponse("Sample this is a End Point", name)

routes = [
    Route("/", HomePage),
    Route("/{username}", User)
]

app = Starlette(routes=routes)