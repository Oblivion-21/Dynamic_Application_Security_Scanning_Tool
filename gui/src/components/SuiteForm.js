import {useRef} from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

function SuiteForm({socket}) {
  const formRef = useRef();
  const tests = [{
      name: "test-test",
      mapKey: "testTest",
      label: "Test Test"
    }, {
      name: "test-test-duplicate",
      mapKey: "testTestDuplicate",
      label: "Test Test Duplicate"
    }, {
      name: "suite-protocol",
      mapKey: "testProtocols",
      testOptions: {
        subTests: [
          "testHttps",
          "testDefaultTls",
          "testTlsVersions",
          "testSelfSignedCertificate",
          "testExpiredCertificate",
          "testWrongHostCertificate",
          "testUntrustedRootCertificate"
        ],
        tlsVersions: [
          "TLSv1.1",
          "TLSv1.2",
          "TLSv1.3"
        ]
      },
      label: "Protocol Versions"
    }
  ];

  const sendSuite = (event) => {
    event.preventDefault();
    const testStr = tests.filter(
      test => formRef.current[test.name].checked
    ).map(
      test => {
        if (test.mapKey === "testProtocols")
          return `"${test.mapKey}": ${JSON.stringify(test.testOptions)}`
        return `"${test.mapKey}": {}`
      }
    ).join();
    const msg = `{
      "message-type": "CREATE-SUITE",
      "url": "${formRef.current["url"].value}",
      "tests": {${testStr}}
    }`;
    console.log(`Message to send: ${msg}`);
    console.log(`Socket state: ${socket.readyState}`);
    if (socket.readyState === 1) socket.send(msg);
  }

  return (
    <Form ref={formRef} className="w-25 py-2 px-4 bg-secondary text-white d-flex flex-column justify-content-between">
      <Form.Group>
        <Form.Label>URL</Form.Label>
        <Form.Control name="url" type="text" placeholder="google.com"/>
      </Form.Group>

      <Form.Group>
        {tests.map((test, index) => (
          <Form.Group key={index} className="bg-primary bg-opacity-50 rounded border border-dark py-2 px-4 my-2">
            <Form.Check className="d-flex justify-content-between" type="checkbox" name={test.name} label={test.label}/>
          </Form.Group>
        ))}
      </Form.Group>
      
      <Button variant="outline-light" className="w-100" onClick={sendSuite}>Submit</Button>
    </Form>
  );
}

export default SuiteForm;
