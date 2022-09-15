import Container from "react-bootstrap/Container";
import Tabs from "react-bootstrap/Tabs";
import Tab from "react-bootstrap/Tab";
import Testing from "./Testing";
import Suites from "./Suites";

function Main({socket}) {
  return (
    <Container fluid className="w-75 py-2 px-0">
      <Tabs defaultActiveKey="testing" className="">
        <Tab eventKey="suites" title="Suites">
          <Suites socket={socket}/>
        </Tab>
        <Tab eventKey="history" title="History">

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
