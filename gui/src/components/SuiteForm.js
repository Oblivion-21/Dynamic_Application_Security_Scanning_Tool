import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

function SuiteForm() {
  const tests = [{
      name: "cool-test",
      label: "Cool Test"
    }, {
      name: "epic-test",
      label: "Epic Test"
    }
  ];

  return (
    <Form className="w-25 py-2 px-4 bg-secondary text-white d-flex flex-column justify-content-between">
      <Form.Group>
        <Form.Label>URL</Form.Label>
        <Form.Control type="text" placeholder="google.com"/>
      </Form.Group>

      <Form.Group>
        {tests.map((test, index) => (
          <Form.Group key={index} className="bg-primary bg-opacity-50 rounded border border-dark py-2 px-4 my-2">
            <Form.Check className="d-flex justify-content-between" type="checkbox" name={test.name} label={test.label}/>
          </Form.Group>
        ))}
      </Form.Group>
      
      <Button variant="outline-light" className="w-100">Submit</Button>
    </Form>
  );
}

export default SuiteForm;
