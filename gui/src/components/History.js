import {useEffect, useState} from "react";
import Button from "react-bootstrap/Button";
import Accordion from "react-bootstrap/Accordion";
import Table from "react-bootstrap/Table";

function History({socket, historyMessage}) {
  const [history, setHistory] = useState([]);

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
    <>
      <Button onClick={updateHistory}>Update History</Button>
      <Accordion className="p-5">
        {history === undefined ? <></> : history.map((suite, index) => (
          <Accordion.Item eventKey={index} key={index}>
            <Accordion.Header>Suite {suite["suiteID"]} | {suite["url"]}</Accordion.Header>
            <Accordion.Body>
              <Table striped bordered hover>
                <tbody>
                  {suite["tests"].map((test, index) => (
                    <tr key={index}>
                      <td>{test}</td>
                      <td>{JSON.stringify(suite[test])}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </Accordion.Body>
          </Accordion.Item>
        ))}
      </Accordion>
    </>
  );
}

export default History;
