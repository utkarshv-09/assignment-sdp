import './App.css';
import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';


function App() {
  const [inputData, setInputData] = useState("");
  const [responseData, setResponseData] = useState("");

  const sendData = () => {
    fetch('http://0.0.0.0:8000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: inputData }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        setResponseData(data.response);
    })
    .catch(error => {
        console.error('Error:', error);
    });
  }

  return (
    <div className="App">
      <input class="inputBox" type="text" placeholder="Ask me something" value={inputData} onChange={(e) => setInputData(e.target.value)} onKeyPress={(e) => { if (e.key === 'Enter') sendData(); }} />
      <div className="messageBox">
      <ReactMarkdown>{responseData}</ReactMarkdown>
      </div>
    </div>
  );
}

export default App;