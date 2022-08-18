import mock
import pytest
import asyncio
import websockets
from pytest_mock import mocker

import TestManager
from tests.protocol import test_https
pytest_plugins = ('pytest_asyncio')

HOST = 'localhost'
PORT = '8989'

@pytest.mark.asyncio
async def test_https_true():
    '''check the https status against a known true'''
    async_mock = mock.AsyncMock()
    mocker.patch('TestManager.send_msg', side_effect=async_mock)
    await test_https.https_test(None, 'www.google.com')

