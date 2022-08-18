import pytest
import asyncio
import websockets
from tests.protocol import test_https
pytest_plugins = ('pytest_asyncio')

HOST = 'localhost'
PORT = '8989'

@pytest.mark.asyncio
async def test_https_true():
    '''check the https status against a known true'''
    async with websockets.connect(f"ws://{HOST}:{PORT}") as ws:
        output = await test_https.https_test(ws, 'www.google.com')
        print(output)
        print(ws)
        output = await ws.recv()
        print(output)
        assert 0==1
