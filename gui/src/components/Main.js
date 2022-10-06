import {useState} from "react";
import Container from "react-bootstrap/Container";
import Tabs from "react-bootstrap/Tabs";
import Tab from "react-bootstrap/Tab";
import Testing from "./Testing";
import Suites from "./Suites";
import History from "./History";

function Main({socket}) {
  const [suiteMessage, setSuiteMessage] = useState("");
  const [historyMessage, setHistoryMessage] = useState("");
  
  socket.onmessage = (event) => {
    const data = event.data;
    const jsonData = JSON.parse(data);
    console.log(`Recived message ${data}`);
    switch (jsonData["messageType"]) {
      case "SUITE-CREATED":
      case "SUITE-STARTED":
      case "TEST-FINISHED":
        setSuiteMessage(jsonData);
        break;
      case "HISTORY":
        setHistoryMessage(jsonData);
        break;
      default:
        break;
    }
  };

  return (
    <Container fluid className="w-75 py-2 px-0">
      <Tabs defaultActiveKey="suites" className="">
        <Tab eventKey="suites" title="Suites">
          <Suites suiteMessage={suiteMessage}/>
        </Tab>
        <Tab eventKey="history" title="History">
          <History socket={socket} historyMessage={historyMessage}/>
        </Tab> 
        <Tab eventKey="analysis" title="Analysis">

        </Tab>
        <Tab eventKey="testing" title="Testing">
          <Testing socket={socket}/>
        </Tab>
      </Tabs>
    </Container>
  );
}

export default Main;
