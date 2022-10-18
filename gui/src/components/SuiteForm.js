import {useRef} from "react";
import {useAccordionButton} from "react-bootstrap/AccordionButton";
import Form from "react-bootstrap/Form";
import Accordion from "react-bootstrap/Accordion";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";

function ConfigButton({children, eventKey}) {
  const configClick = useAccordionButton(eventKey);
  return (<Button onClick={configClick}>{children}</Button>);
}

function SuiteForm({socket}) {
  // Test name strings
  const bruteForceName = "brute-force-test";
  const ddosName = "test-ddos";
  const xssName = "xss";
  const ssrfName = "test-ssrf";
  const suiteProtocolName = "suite-protocol";
  // Test config label strings
  const bruteForceUsername = "bruteForceUsername";
  const ddosDuration = "ddosDuration";
  const testHttps = "testHttps";
  const testDefaultTls = "testDefaultTls";
  const testTlsVersions = "testTlsVersions";
  const testSelfSignedCertificate = "testSelfSignedCertificate";
  const testExpiredCertificate = "testExpiredCertificate";
  const testWrongHostCertificate = "testWrongHostCertificate";
  const testUntrustedRootCertificate = "testUntrustedRootCertificate";
  const TLSv11 = "TLSv1.1";
  const TLSv12 = "TLSv1.2";
  const TLSv13 = "TLSv1.3";

  const formRef = useRef();
  const tests = [
    {
      name: bruteForceName,
      mapKey: "bruteForceTest",
      label: "Brute Force"
    }, {
      name: ddosName,
      mapKey: "testDdos",
      label: "DDoS"
    }, {
      name: xssName,
      mapKey: "xss",
      label: "XSS"
    }, { 
      name: ssrfName,
      mapKey: "testSSRF",
      label: "SSRF"
    }, {
      name: suiteProtocolName,
      mapKey: "testProtocols",
      label: "Protocol Versions"
    }, { 
      name: "test-logging",
      mapKey: "testLogging",
      label: "Logging"
    }
  ];

  const sendSuite = (event) => {
    event.preventDefault();
    const testStr = tests.filter(
      test => formRef.current[test.name].checked
    ).map(
      test => {
        switch (test.name) {
          case bruteForceName:
            return `"${test.mapKey}": {
              "username": "${formRef.current[bruteForceUsername].value}"
            }`;
          case ddosName:
            return `"${test.mapKey}": {
              "ddosDuration": "${formRef.current[ddosDuration].value}"
            }`;
          case suiteProtocolName:
            const subTests = [
              formRef.current[testHttps].checked ? testHttps : null,
              formRef.current[testDefaultTls].checked ? testDefaultTls : null,
              formRef.current[testTlsVersions].checked ? testTlsVersions: null,
              formRef.current[testSelfSignedCertificate].checked ? testSelfSignedCertificate : null,
              formRef.current[testExpiredCertificate].checked ? testExpiredCertificate : null,
              formRef.current[testWrongHostCertificate].checked ? testWrongHostCertificate : null,
              formRef.current[testUntrustedRootCertificate].checked ? testUntrustedRootCertificate : null
            ].filter(subTest => subTest != null);
            const tlsVersions = [
              formRef.current[TLSv11].checked ? TLSv11 : null,
              formRef.current[TLSv12].checked ? TLSv12 : null,
              formRef.current[TLSv13].checked ? TLSv13 : null
            ].filter(tlsVersion => tlsVersion != null);
            return `"${test.mapKey}": {
              "subTests": ${JSON.stringify(subTests)},
              "tlsVersions": ${JSON.stringify(tlsVersions)}
            }`;
          default:
        }
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

  const testConfig = (test) => {
    switch (test.name) {
      case bruteForceName:
        return (
          <Card.Body align="left">
            <Form.Label>Form Username</Form.Label>
            <Form.Control type="text" defaultValue="admin" name={bruteForceUsername} required/>
          </Card.Body>
        );
      case ddosName:
        return (
          <Card.Body align="left">
            <Form.Label>DDoS Duration (Seconds)</Form.Label>
            <Form.Control type="number" defaultValue={30} name="ddosDuration" required/>
          </Card.Body>
        );
      case suiteProtocolName:
        return (
          <Card.Body align="left">
            <Form.Label>Sub Tests</Form.Label>
            <Form.Group>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="testHttps" label="Test Https"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="testDefaultTls" label="Test Default TLS"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="testTlsVersions" label="Test TLS Versions"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="testSelfSignedCertificate" label="Test Self Signed Certificate"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="testExpiredCertificate" label="Test Expired Certificate"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="testWrongHostCertificate" label="Test Wrong Host Certificate"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="testUntrustedRootCertificate" label="Test Untrusted Root Certificate"/>
            </Form.Group>
            <Form.Label>TLS Versions</Form.Label>
            <Form.Group className="d-flex flex-column">
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="TLSv1.1" label="TLSv1.1"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="TLSv1.2" label="TLSv1.2"/>
              <Form.Check type="checkbox" className="d-flex align-items-center" defaultChecked name="TLSv1.3" label="TLSv1.3"/>
            </Form.Group>
          </Card.Body>
        );
      default:
    }
    return (<Card.Body align="left">NO CONFIG AVALIBLE</Card.Body>);
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
      
      <Accordion align="center">
        {tests.map((test, index) => (
          <Card eventKey={index} key={index} className="bg-primary bg-opacity-25 font-weight-bold text-light rounded border border-primary py-1 px-2 my-2">
            <Card.Header className="d-flex justify-content-between align-items-center">
              <Form.Check className="d-flex align-items-center text-nowrap px-4" type="checkbox" name={test.name} label={test.label}/>
              <ConfigButton eventKey={index}>&#11167;</ConfigButton>
            </Card.Header>
            <Accordion.Collapse eventKey={index}>
              {testConfig(test)}
            </Accordion.Collapse>
          </Card>
        ))}
      </Accordion>
      
      <Button align="center" variant="success" className="mb-1 w-100" onClick={sendSuite}>Submit</Button>
      
    </Form>
  );
}

export default SuiteForm;
