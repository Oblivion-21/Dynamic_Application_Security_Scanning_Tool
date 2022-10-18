import Accordion from 'react-bootstrap/Accordion';
import Table from 'react-bootstrap/Table';

const accordionOutstyle = {
    overflowY: "scroll",
    height: "92vh",
    maxHeight: "92vh",
  }

function Sites() {
    return (
        <div>
        <Accordion className="accordion accordion-flush" style={accordionOutstyle}>
        <Accordion.Item eventKey="0">
            <Accordion.Header>SSRF</Accordion.Header>
            <Accordion.Body>
            <Table striped>
                <thead>
                    <tr>
                        <th>Expected Result</th>
                        <th>Site Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Pass</td>
                        <td>https://github.com/Oblivion-21/Dynamic_Application_Security_Scanning_Tool/</td>
                    </tr>
                    <tr>
                        <td>Fail</td>
                        <td>http://169.254.169.254/</td>
                    </tr>
                    <tr>
                        <td>Invalid</td>
                        <td>https://github.com/Oblivion-21/Dynamic_Application_Security_Scanning_Tool/</td>
                    </tr>
                </tbody>
            </Table>
            </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="1">
            <Accordion.Header>XSS</Accordion.Header>
            <Accordion.Body>
            <Table striped>
                <thead>
                    <tr>
                        <th>Expected Result</th>
                        <th>Site Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Pass</td>
                        <td>https://github.com/Oblivion-21/Dynamic_Application_Security_Scanning_Tool</td>
                    </tr>
                    <tr>
                        <td>Fail</td>
                        <td>https://xss-game.appspot.com/level1/frame</td>
                    </tr>
                    <tr>
                        <td>Incomplete</td>
                        <td>https://google.com</td>
                    </tr>
                </tbody>
            </Table>
            </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="2">
            <Accordion.Header>Authentication</Accordion.Header>
            <Accordion.Body>
            <Table striped>
                <thead>
                    <tr>
                        <th>Expected Result</th>
                        <th>Site Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Pass</td>
                        <td>https://s1.swin.edu.au/eStudent/login.aspx</td>
                    </tr>
                    <tr>
                        <td>Fail</td>
                        <td>www.team17.com/wp-login.php</td>
                    </tr>
                    <tr>
                        <td>Invalid</td>
                        <td>google.com</td>
                    </tr>
                </tbody>
            </Table>
            </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="3">
            <Accordion.Header>DDoS</Accordion.Header>
            <Accordion.Body>
            <Table striped>
                <thead>
                    <tr>
                        <th>Expected Result</th>
                        <th>Site Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Pass</td>
                        <td>www.google.com</td>
                    </tr>
                    <tr>
                        <td>Fail</td>
                        <td>www.gdsadsadsadsaoogle.com</td>
                    </tr>
                </tbody>
            </Table>
            </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="4">
            <Accordion.Header>Site Map</Accordion.Header>
            <Accordion.Body>
            <Table striped>
                <thead>
                    <tr>
                        <th>Expected Result</th>
                        <th>Site Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>
            </Table>
            </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="5">
            <Accordion.Header>Logging</Accordion.Header>
            <Accordion.Body>
            <Table striped>
                <thead>
                    <tr>
                        <th>Expected Result</th>
                        <th>Site Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Pass</td>
                        <td>google.com</td>
                    </tr>
                    <tr>
                        <td>Fail</td>
                        <td>https://liveswinburneeduau-my.sharepoint.com/:u:/g/personal/102568843_student_swin_edu_au/Efh1aNATAp9Avm_9N4-EUFIBEfS7q6VWpkE7byjxRZr_ug?e=h71kNn</td>
                    </tr>
                    <tr>
                        <td>Invalid</td>
                        <td>badwebsite.com</td>
                    </tr>
                </tbody>
            </Table>
            </Accordion.Body>
        </Accordion.Item>
        </Accordion>
        </div>
    )
}

export default Sites;
