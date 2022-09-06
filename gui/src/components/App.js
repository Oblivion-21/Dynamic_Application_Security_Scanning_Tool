import Container from "react-bootstrap/Container";
import SuiteForm from "./SuiteForm";
import Main from "./Main";

function App() {
  const socket = new WebSocket("ws://localhost:8989");
  socket.addEventListener('message', (event) => {
    const data = event.data;
    console.log(`Recived message ${data}`);
    document.getElementById("testing-out").innerHTML += `<div class="data">${data}</div>`;
  });

  return (
    <Container fluid className="h-100 mh-100 m-0 p-0 d-flex">
      <Main socket={socket}/>
      <SuiteForm socket={socket}/>      
    </Container>
  );
}

export default App;
