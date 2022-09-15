import asyncio
import threading

from websockets import serve

import testManager

host = "127.0.0.1"
port = 8989
processLock = threading.Lock()


async def messageHand(ws):
    async for msg in ws:
        with processLock:
            await testManager.runTests(ws, msg)


async def sendMessage(ws, msg):
    await ws.send(msg)


async def server():
    async with serve(messageHand, host, port):
        await asyncio.Future()


if __name__ == "__main__":
    print(f"Websocket API running: {host}:{port}")
    asyncio.run(server())
