import Container from "react-bootstrap/Container";
import SuiteForm from "./SuiteForm";
import Main from "./Main";

function App() {
  return (
    <Container fluid className="h-100 mh-100 m-0 p-0 d-flex">
      <Main/>
      <SuiteForm/>      
    </Container>
  );
}

export default App;
