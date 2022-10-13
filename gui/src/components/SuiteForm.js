import {useRef} from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

function SuiteForm({socket}) {
  const formRef = useRef();
  const tests = [{
      name: "brute-force-test",
      mapKey: "bruteForceTest",
      label: "Brute Force",
      testOptions: {
        username: "admin"
      }
    }, {
      name: "test-ddos",
      mapKey: "testDdos",
      label: "DDoS",
      testOptions: {
        ddosDuration: "30"
      }
    }, {
      name: "xss",
      mapKey: "xss",
      label: "XSS"
    }, { 
      name: "test-ssrf",
      mapKey: "testSSRF",
      label: "SSRF"
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
        if (test.mapKey === "bruteForceTest" || test.mapKey === "testProtocols" || test.mapKey === "testDdos")
          return `"${test.mapKey}": ${JSON.stringify(test.testOptions)}`
        return `"${test.mapKey}": {}`
      }
    ).join();
    const msg = `{
      "messageType": "CREATE-SUITE",
      "url": "${formRef.current["url"].value}",
      "tests": {${testStr}}
    }`;
    console.log(`Message to send: ${msg}`);
    console.log(`Socket state: ${socket.readyState}`);
    if (socket.readyState === 1) socket.send(msg);
  };

  return (
    <Form ref={formRef} className="py-2 px-3 bg-dark text-white d-flex flex-column justify-content-between">
      <Form.Group align="center">
        <hr />
        <Form.Label><h3>OPTIONS</h3></Form.Label>
        <hr className = "mt-1" />
        <Form.Control name="url" type="text" placeholder="Enter a URL"/>
        <hr />
      </Form.Group>
      
      <Form.Group align="center">
        {tests.map((test, index) => (
          <Form.Group key={index} className="bg-primary bg-opacity-25 text-right font-weight-bold text-light rounded border border-primary py-1 px-2 my-2 text-nowrap" align="right">
            <Form.Check className="d-flex justify-content-between" type="checkbox" name={test.name} label={test.label}/>
          </Form.Group>
        ))}
      </Form.Group>
      
      <Button align="center" variant="success" className="mb-1 w-100" onClick={sendSuite}>Submit</Button>
      
    </Form>
  );
}

export default SuiteForm;
