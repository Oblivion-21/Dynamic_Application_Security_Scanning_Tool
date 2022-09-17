import asyncio
import json
import threading

from websockets import serve

import storageManager
import testManager

host = "127.0.0.1"
port = 8989
processLock = threading.Lock()
useDatabase = False


async def messageHand(ws):
    async for msg in ws:
        if json.loads(msg)["messageType"] == "REQ-HISTORY":
            await history(ws)
        else:
            with processLock:
                await testManager.runTests(ws, msg, useDatabase)


async def sendMessage(ws, msg):
    await ws.send(msg)


async def server():
    async with serve(messageHand, host, port):
        await asyncio.Future()


async def history(ws):
    history = {
        "messageType": "HISTORY",
        "results": storageManager.show()
    }
    await sendMessage(ws, json.dumps(history))


if __name__ == "__main__":
    useDatabase = storageManager.setup()
    if useDatabase:
        testManager.setSuiteID()
    print(f"Websocket API running: {host}:{port}")
    asyncio.run(server())
