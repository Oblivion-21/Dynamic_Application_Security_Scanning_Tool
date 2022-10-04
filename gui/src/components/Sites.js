import Accordion from 'react-bootstrap/Accordion';
import Table from 'react-bootstrap/Table';

function Sites() {
    return (
        <Accordion defaultActiveKey="0">
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
                        <td>https://soundcloud.com/discover/sets/track-stations:443037147</td>
                    </tr>
                    <tr>
                        <td>Pass</td>
                        <td>https://github.com/Oblivion-21/Dynamic_Application_Security_Scanning_Tool/branches/active</td>
                    </tr>
                    <tr>
                        <td>Fail</td>
                        <td>http://testhtml5.vulnweb.com/#/popular</td>
                    </tr>
                    <tr>
                        <td>Fail</td>
                        <td>https://xss-game.appspot.com/level1/frame</td>
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
        </Accordion>
    )
}

export default Sites;
