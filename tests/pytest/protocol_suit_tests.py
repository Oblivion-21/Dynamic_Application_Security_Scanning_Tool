import pytest
import asyncio
import sys
import os

# print(os.getcwd())
sys.path.append('..')

# from protocol import test_https
import protocol.test_https
pytest_plugins = ('pytest_asyncio')


@pytest.mark.asyncio
async def test_https_true():
    '''check the https status against a known true'''
    print(await https_test('', 'www.google.com'))

def test_test_function_2():
    output = test_function(2)
    assert output == 3
