import {useCallback, useEffect, useState} from "react";
import Accordion from "react-bootstrap/Accordion";
import Table from "react-bootstrap/Table";

function Suites({suiteMessage}) {
  const [suites, setSuite] = useState({});
  
  const addAndUpdateSuites = useCallback((jsonData) => {
    switch (jsonData["messageType"]) {
      case "SUITE-CREATED":
      case "SUITE-STARTED":
        const newSuite = {[jsonData["suiteID"]]: jsonData};
        setSuite(suites => ({
          ...suites,
          ...newSuite
        }));
        break;
      case "TEST-FINISHED":
        const updatedData = {[jsonData["suiteID"]]: suites[jsonData["suiteID"]]};
        updatedData[jsonData["suiteID"]][jsonData["test"]] = jsonData["results"];
        setSuite(suites => ({
          ...suites,
          ...updatedData
        }));
        break;
      default:
        break;
    }
  }, [suites, setSuite]);
  
  useEffect(() => addAndUpdateSuites(suiteMessage), [suiteMessage]);

  return (
    <Accordion className="p-5">
      {Object.entries(suites).map((suite, index) => (
        <Accordion.Item eventKey={index} key={index}>
          <Accordion.Header>Suite {suite[1]["suiteID"]} | {suite[1]["url"]}</Accordion.Header>
          <Accordion.Body>
            <Table striped bordered hover>
              <tbody>
                {suite[1]["tests"].map((test, index) => (
                  <tr key={index}>
                    <td>{test}</td>
                    <td>{JSON.stringify(suite[1][test])}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </Accordion.Body>
        </Accordion.Item>
      ))}
    </Accordion>
  );
}

export default Suites;
