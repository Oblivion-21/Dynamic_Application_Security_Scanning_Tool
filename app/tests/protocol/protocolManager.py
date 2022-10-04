from . import testHttps
from . import testSsl
from . import testCertificates

async def testToRun(ws, session, testConfigs, url, useDatabase):
    runningTests = testConfigs['subTests']

    if 'testHttps' in runningTests:
        await testHttps.testHttps(ws, session, url, useDatabase)

    if 'testDefaultTls' in runningTests:
        await testSsl.testDefaultTls(ws, url, useDatabase)

    if 'testTlsVersions' in runningTests:
        for version in testConfigs['tlsVersions']:
            await testSsl.testTlsVersion(ws, url, version, useDatabase)

    if 'testSelfSignedCertificate' in runningTests:
        await testCertificates.testSelfSignedCertificate(ws, url, useDatabase)

    if 'testExpiredCertificate' in runningTests:
        await testCertificates.testExpiredCertificate(ws, url, useDatabase)

    if 'testWrongHostCertificate' in runningTests:
        await testCertificates.testWrongHostCertificate(ws, url, useDatabase)

    if 'testUntrustedRootCertificate' in runningTests:
        await testCertificates.testUntrustedRootCertificate(ws, url, useDatabase)
