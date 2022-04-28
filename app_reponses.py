import asyncio
from contextlib import AsyncExitStack
from urllib import request, response
from starlette.responses import Response, HTMLResponse, JSONResponse, RedirectResponse , PlainTextResponse, StreamingResponse
from starlette.requests import Request


async def app(scope, recieve, send):
    assert scope["type"] == "http"
    response = Response("HELLO KEVS", media_type="text/plain")
    await response(scope, recieve, send)


async def app_html(scope, receive, send):
    assert scope["type"] == "http"
    response = HTMLResponse("<H1>Testing HTML</H!>")
    await response(scope, receive, send)


# return JSON TYPE
async def app_json(scope, receive, send):
    assert scope["type"] == "http"
    request = Request(scope, receive)
    data = {"message": "Testing Success", "status": f"{request.method}"}
    response = JSONResponse(data)
    await response(scope, receive, send)

async def app_redirect(scope, receive, send): 
    assert scope['scope']  == 'http'
    if scope['path'] != '/':
        response = RedirectResponse(url='/')
    else: 
        response = PlainTextResponse('Hello pre!')
    await response(scope, receive, send)


async def slow_counting(min, max): 
    yield('<html><body><ul>')
    for num in range(min, max+1): 
        yield f'<li>{num}</li>'
        await asyncio.sleep(0.5)
    yield('</ul></body><html>')


async def app_streaming(scope, receive, send):
    assert scope['type'] == 'http'
    generate_data = slow_counting(1,10)
    response = StreamingResponse(generate_data, media_type='text/html')
    await response(scope, receive, send)


