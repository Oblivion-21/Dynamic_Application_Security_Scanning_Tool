from . import testHttps
from . import testSsl
import asyncio

async def testToRun(ws, session, testConfigs, url):
    runningTests = testConfigs['subTests']

    if 'testHttps' in runningTests:
        await testHttps.testHttps(ws, session, url)

    if 'testDefaultTls' in runningTests:
        await testSsl.testDefaultTls(ws, url)

    if 'testTlsVersions' in runningTests:
        for version in testConfigs['tlsVersions']:
            await testSsl.testTlsVersion(ws, url, version)
