import {useEffect, useState, useRef} from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import {Form, Table} from "react-bootstrap";
import {Pie, PieChart, Cell, ResponsiveContainer, PolarGrid, PolarAngleAxis, Radar, Legend, RadarChart, PolarRadiusAxis} from "recharts";

function Analysis({socket, analysisMessage}) {
  const formRef = useRef();
  const [analysis, setAnalysis] = useState("");
  const [analysisView, setAnalysisView] = useState(<></>);

  useEffect(() => {
    if (!analysisMessage["results"]) return;
    setAnalysis(analysisMessage["results"]);
    setAnalysisView(convertToView(analysis));
  }, [analysisMessage, analysis]);

  const updateAnalysis = (event) => {
    event.preventDefault();
    const msg = `{
      "messageType": "REQ-ANALYSIS",
      "url": "${formRef.current["url"].value}"
    }`;
    console.log(`Socket state: ${socket.readyState}`);
    if (socket.readyState === 1) socket.send(msg);
  };

  const viewStyle = {
    height: "90%",
    minHeight: "90%"
  };
  const scoreStyle = {
    height: "10%",
    minHeight: "10%"
  };
  const tableStyle = {
    height: "40%",
    minHeight: "40%"
  };
  const colors = ['#44af69', '#f8333c', '#fcab10', '#2b9eb3'];
  const radian = Math.PI / 180;

  const renderCustomizedLabel = ({ cx, cy, midAngle, innerRadius, outerRadius, percent, index }) => {
    const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
    const x = cx + radius * Math.cos(-midAngle * radian);
    const y = cy + radius * Math.sin(-midAngle * radian);

    return (
      <text x={x} y={y} fill="white" textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central">
        {percent > 0.10 ? `${(percent * 100).toFixed(0)}%`: ``}
      </text>
    );
  };

  const convertToView = (analysis) => {
    if (analysis.length == 0) return <></>;    
    return (
      <Container className="w-100 mw-100 p-0" style={viewStyle}>
        <h3 className="w-100 mw-100 p-0 m-0 d-flex justify-content-center align-items-center" style={scoreStyle}>Final Score: {analysis["overallScore"]} / 100</h3>
        <Container className="w-100 mw-100 p-0 h-50 mh-50">
          <ResponsiveContainer width="50%" className="d-inline-block">
            <PieChart width="100%">
              <Pie
                labelLine={false}
                label={renderCustomizedLabel}
                data={analysis["msgCount"].filter((data) => data["value"] != 0)} 
                outerRadius={100}
                fill="#8884d8"
                dataKey="value"
              >
                {analysis["msgCount"].map((_, index) => (
                  <Cell key={index} fill={colors[index % colors.length]} />
                ))}
              </Pie>
              <Legend layout="vertical"/>
            </PieChart>
          </ResponsiveContainer>
          <ResponsiveContainer width="50%" className="d-inline-block">
            <RadarChart outerRadius={90} data={analysis["testCount"]}>
              <PolarGrid/>
              <PolarAngleAxis dataKey="name"/>
              <PolarRadiusAxis angle={30}/>
              <Radar name="Run Count" dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
              <Legend/>
            </RadarChart>
          </ResponsiveContainer>
        </Container>
        <Container className="w-100 mw-100 p-0 d-flex flex-column justify-content-center" style={tableStyle}>
          <Table striped bordered hover>
            <tbody>
              <tr>
                {analysis["msgCount"].map((data, index) => <th key={index}>{data["name"]}</th>)}
              </tr>
              <tr>
                {analysis["msgCount"].map((data, index) => <td key={index}>{data["value"]}</td>)}
              </tr>
            </tbody>
          </Table>
          <Table striped bordered hover>
            <tbody>
              <tr>
                {analysis["testCount"].map((data, index) => <th key={index}>{data["name"]}</th>)}
              </tr>
              <tr>
                {analysis["testCount"].map((data, index) => <td key={index}>{data["value"]}</td>)}
              </tr>
            </tbody>
          </Table>
        </Container>
      </Container>
    );
  };

  const formStyle = {
    minHeight: "10%"
  };

  return (
    <Container fluid className="p-5 h-100 mh-100 w-100 mw-100">
      <Form ref={formRef} className="d-grid gap-4 w-100 mw-100" style={formStyle}>
        <Form.Group align="left">
          <Form.Label>URL</Form.Label>
          <Form.Control name="url" type="text" placeholder="Enter a URL" required/>
        </Form.Group>
        <Button onClick={updateAnalysis}>Update Analysis</Button>
      </Form>
      {analysisView}
    </Container>
  );
}

export default Analysis;
