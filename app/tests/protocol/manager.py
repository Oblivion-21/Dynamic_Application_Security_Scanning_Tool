from . import testHttps
from . import testSsl
from . import testCertificates
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

    if 'testSelfSignedCertificate' in runningTests:
        await testCertificates.testSelfSignedCertificate(ws, url)

    if 'testExpiredCertificate' in runningTests:
        await testCertificates.testExpiredCertificate(ws, url)

    if 'testWrongHostCertificate' in runningTests:
        await testCertificates.testWrongHostCertificate(ws, url)

    if 'testUntrustedRootCertificate' in runningTests:
        await testCertificates.testUntrustedRootCertificate(ws, url)
