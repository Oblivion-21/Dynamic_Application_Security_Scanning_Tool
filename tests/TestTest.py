import TestManager


async def test_test(ws):
    await TestManager.send_msg(ws, {"message": "Hello Test!"}, True, "test-test")
