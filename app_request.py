from urllib import request
from starlette.requests import Request
from starlette.responses import Response


async def app(scope, receive, send): 
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    content = f'{request.method} - {request.url.path}'
    reponse = Response(content, media_type='text/plain')
    await reponse(scope, receive, send)

