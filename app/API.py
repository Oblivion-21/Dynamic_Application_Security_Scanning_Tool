import asyncio
import json
import threading

from websockets import serve

import analysisManager
import storageManager
import testManager

host = "back_end"
port = 8989
processLock = threading.Lock()
useDatabase = False


async def messageHand(ws):
    async for msg in ws:
        msgJson = json.loads(msg)
        if msgJson["messageType"] == "REQ-HISTORY":
            # TODO: If no database exists send an appropriate message to GUI
            if useDatabase:
                await history(ws)
        elif msgJson["messageType"] == "REQ-ANALYSIS":
            await analysis(ws, msgJson["url"])
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


async def analysis(ws, url):
    analysis = {
        "messageType": "ANALYSIS",
        "results": analysisManager.analyse(url)
    }
    await sendMessage(ws, json.dumps(analysis))


if __name__ == "__main__":
    useDatabase = False
    try:
        useDatabase = storageManager.setup()
    except Exception as e:
        print(f"Setting up database failed with: {e}")
    if useDatabase:
        testManager.setSuiteID()
    print(f"Websocket API running: {host}:{port}")
    asyncio.run(server())
