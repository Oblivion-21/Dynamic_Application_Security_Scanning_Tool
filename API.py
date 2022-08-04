import asyncio
import threading

from websockets import serve

import TestManager

process_lock = threading.Lock()


async def msg_hand(ws):
    async for msg in ws:
        with process_lock:
            await TestManager.test_manager(ws, msg)


async def send_msg(ws, msg):
    await ws.send(msg)


async def server():
    async with serve(msg_hand, "localhost", 8989):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(server())
