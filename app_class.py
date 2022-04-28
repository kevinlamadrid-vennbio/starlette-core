from email import message
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse 
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

def mainpage(request):
    return PlainTextResponse('Hello, world!')
def user_me(request):
    username = request.path_params['username']
    return PlainTextResponse('Hello, %s!' % username)

async def websocket_endpoint(websocket): 
    await websocket.accept()
    await websocket.send_text("Hello ista me WEBSOCKET")
    await websocket.close()


def startup():
    print('Ready to go')


routes = [
    Route('/', mainpage),
    Route('/user/{username}', user_me),
    WebSocketRoute('/ws', websocket_endpoint),
    Mount('/static', StaticFiles(directory="static")),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
# app.state.ADMIN_EMAIL = 'admin@example.org'
