from mock import mock

import storageManager


def testSetupWithException(mocker):
    # SETUP
    mocker.patch("storageManager.databaseExec", side_effect=Exception("Test exception"))

    success = storageManager.setup()
    assert success is False

    # TEARDOWN
    mocker.stopall()


def testDataExecWithNonFile(mocker):
    # SETUP
    connectMock = mock.MagicMock()
    cursorMock = mock.Mock()
    mocker.patch("psycopg2.connect", side_effect=connectMock)
    connectMock.attach_mock(cursorMock, "cursor")

    try:
        storageManager.databaseExec("I AM NOT A FILE")
    except Exception as e:
        assert type(e) is FileNotFoundError

    # TEARDOWN
    mocker.stopall()


def testShowWithEmptyRes(mocker):
    # SETUP
    executeMock = mock.Mock()
    mocker.patch("storageManager.databaseExec", side_effect=executeMock)
    executeMock.return_value = []

    out = storageManager.show()
    assert out == []

    # TEARDOWN
    mocker.stopall()


def testShowWithNormalRes(mocker):
    # SETUP
    resJson = '{"cool": "epic"}'
    executeMock = mock.Mock()
    mocker.patch("storageManager.databaseExec", side_effect=executeMock)
    executeMock.return_value = [[resJson], [resJson], [resJson]]

    out = storageManager.show()
    assert out == [resJson, resJson, resJson]

    # TEARDOWN
    mocker.stopall()


def testCurrentIdentityWithEmptyRes(mocker):
    # SETUP
    executeMock = mock.Mock()
    mocker.patch("storageManager.databaseExec", side_effect=executeMock)
    executeMock.return_value = []

    out = storageManager.currentIdentity()
    assert out == 0

    # TEARDOWN
    mocker.stopall()


def testCurrentIdentityWithNormalRes(mocker):
    # SETUP
    resId = 500
    executeMock = mock.Mock()
    mocker.patch("storageManager.databaseExec", side_effect=executeMock)
    executeMock.return_value = [[resId]]

    out = storageManager.currentIdentity()
    assert out == resId

    # TEARDOWN
    mocker.stopall()
