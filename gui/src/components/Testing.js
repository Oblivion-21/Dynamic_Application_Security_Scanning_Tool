import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";

function Testing() {
  const connectAndSend = (e) => {
    e.preventDefault();
    console.log("Test button pressed");
    const socket = new WebSocket("ws://localhost:8989");

    socket.addEventListener('open', () => {
      const msg = `{
          "message-type": "CREATE-SUITE",
          "url": "http://google.com",
          "tests": {
              "testTest": {},
              "testTestDuplicate": {}
          }
      }`;
      socket.send(msg);
      console.log("Sent CREATE-SUITE message");
    });

    socket.addEventListener('message', (e) => {
      const data = e.data;
      console.log(`Recived message ${data}`);
      document.getElementById("testing-out").innerHTML += `<div class="data">${data}</div>`;
    });
  }
  const testingOutstyle = {
    overflowY: "scroll",
    height: "75vh",
    maxHeight: "75vh",
  }

  return (
    <Container fluid className="p-4 d-grid gap-4">
      <Button variant="primary" onClick={connectAndSend}>Connect & Send</Button>
      <div id="testing-out" style={testingOutstyle}></div>
    </Container>
  );
}

export default Testing;
