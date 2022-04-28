import asyncio
import websockets

async def message(): 
    async with websockets.connect("ws://127.0.0.1:8000") as socket: 
        message = input("Message me pls: ")
        await socket.send(message) 
        print(await socket.recv())
asyncio.get_event_loop().run_until_complete(message())


#please run uvicorn ws:app and python app_web_socket_message.py