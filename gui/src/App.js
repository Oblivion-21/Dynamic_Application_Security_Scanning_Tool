import Container from "react-bootstrap/Container";
import Tabs from "react-bootstrap/Tabs";
import Tab from "react-bootstrap/Tab";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

function App() {
  const tests = [{
      id: "cool-test",
      label: "Cool Test"
    }, {
      id: "epic-test",
      label: "Epic Test"
    }
  ];
  
  return (
    <Container fluid className="h-100 mh-100 m-0 p-0 d-flex">
      <Container fluid className="w-75 py-2 px-0">
        <Tabs defaultActiveKey="testing" className="">
          <Tab eventKey="suites" title="Suites">

          </Tab>
          <Tab eventKey="history" title="History">

          </Tab> 
          <Tab eventKey="analysis" title="Analysis">

          </Tab>
          <Tab eventKey="testing" title="Testing">
            <Button variant="primary" id="test-button">Connect & Send</Button>
            <div id="testing-out"></div>
          </Tab>
        </Tabs>
      </Container>
      <Form className="w-25 py-2 px-4 bg-secondary text-white d-flex flex-column justify-content-between">
        <Form.Group>
          <Form.Label>URL</Form.Label>
          <Form.Control type="text" placeholder="google.com"/>
        </Form.Group>

        <Form.Group>
          {tests.map((test) => (
            <Form.Group className="bg-primary bg-opacity-50 rounded py-2 px-4 my-2">
              <Form.Check className="d-flex justify-content-between" type="checkbox" id={test.id} label={test.label}/>
            </Form.Group>
          ))}
        </Form.Group>
        
        <Button variant="outline-light" className="w-100">Submit</Button>
      </Form>
    </Container>
  );
}

export default App;
