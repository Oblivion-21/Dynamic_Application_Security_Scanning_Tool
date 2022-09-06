import Container from "react-bootstrap/Container";

function Testing({socket}) {
  socket.addEventListener('message', (event) => {
    const data = event.data;
    console.log(`Recived message ${data}`);
    document.getElementById("testing-out").innerHTML += `<div class="data">${data}</div>`;
  });
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
