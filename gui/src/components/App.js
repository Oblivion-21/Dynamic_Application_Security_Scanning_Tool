import {useState} from "react";
import Container from "react-bootstrap/Container";
import SuiteForm from "./SuiteForm";
import Main from "./Main";

function App() {
  const [socket] = useState(new WebSocket(`ws://${[process.env.REACT_APP_BACK_END]}:8989`));
  return (
    <Container fluid className="vh-100 min-vh-100 vw-100 min-vw-100 m-0 p-0 d-flex">
      <Main socket={socket}/>
      <SuiteForm socket={socket}/>    
    </Container>
  );
}

export default App;
