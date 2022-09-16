import Container from "react-bootstrap/Container";

function Testing() {
  const testingOutstyle = {
    overflowY: "scroll",
    height: "75vh",
    maxHeight: "75vh",
  }
  return (
    <Container fluid className="p-4 d-grid gap-4">
      <div id="testing-out" style={testingOutstyle}></div>
    </Container>
  );
}

export default Testing;
