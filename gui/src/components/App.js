import {useState} from "react";
import Container from "react-bootstrap/Container";
import SuiteForm from "./SuiteForm";
import Main from "./Main";

function App() {
  const [socket] = useState(new WebSocket("ws://172.22.0.3:8989"));
  return (
    <Container fluid className="h-100 mh-100 m-0 p-0 d-flex">
      <Main socket={socket} className="h-100 mh-100"/>
      <SuiteForm socket={socket} className="h-100 mh-100"/>    
    </Container>
  );
}

export default App;
