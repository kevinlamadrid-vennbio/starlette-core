from starlette.applications import Starlette
from starlette.responses import JSONResponse 
from starlette.routing import Route 
from starlette.status import HTTP_200_OK
from starlette.responses import PlainTextResponse

async def mainpage(request): 
    data = {
        'message' : "Testing Successfully",
        'status': HTTP_200_OK
    }
    return JSONResponse(data)



async def testing(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)

#
# Routing
#

# app = Starlette(debug=True, routes=[
#     Route('/', mainpage),
#     Route('testing', testing)
# ])



from starlette.responses import PlainTextResponse
async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)




