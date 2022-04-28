from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def home(request):
    return PlainTextResponse("This is Just a Home")


async def about(request): 
    return PlainTextResponse("This for about Phase")


async def users(request): 
    username = request.path_params['username']
    return PlainTextResponse(f"This for about Phase , {username}")


route = [
    Route("/", endpoint=home),
    Route("/about", endpoint=about, methods=['GET']),
    Route("/users/{username}", endpoint=users)

]

app = Starlette(routes=route)

# https://www.starlette.io/routing/