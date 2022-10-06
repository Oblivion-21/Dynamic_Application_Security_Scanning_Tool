import {useEffect, useState} from "react";
import Button from "react-bootstrap/Button";
import Accordion from "react-bootstrap/Accordion";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";

function History({socket, historyMessage}) {
  const [history, setHistory] = useState([]);
  const dontPrint = ["messageType", "url", "suiteID", "tests"];

  useEffect(() => setHistory(historyMessage["results"]), [historyMessage]);

  const updateHistory = (event) => {
    event.preventDefault();
    const msg = `{
      "messageType": "REQ-HISTORY"
    }`;
    console.log(`Socket state: ${socket.readyState}`);
    if (socket.readyState === 1) socket.send(msg);
  };

  return (
    <Container fluid className="p-5 d-grid gap-4">
      <Button onClick={updateHistory}>Update History</Button>
      <Accordion>
        {history === undefined ? <></> : history.map((run, index) => (
          <Accordion.Item eventKey={index} key={index}>
            <Accordion.Header>Run {run["suiteID"]} | {run["url"]}</Accordion.Header>
            <Accordion.Body>
              <Table striped bordered hover>
                <tbody>
                  {Object.keys(run)
                  .filter((print) => !dontPrint.includes(print))
                  .map((key, index) => (
                    <tr key={index}>
                      <td>{key}</td>
                      <td>{JSON.stringify(run[key])}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </Accordion.Body>
          </Accordion.Item>
        ))}
      </Accordion>
    </Container>
  );
}

export default History;
