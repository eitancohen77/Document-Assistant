import React, { useState, useEffect } from 'react'

function App() {

  const [input, setInput] = useState('')
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/manipulateData", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userInput: input }),
      });
      const data = await response.json();
      setResult(data.processedData);
    } catch (error) {
      console.error("Error:", error);
    }
  };


  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      <p>AI Response {result}</p>
    </div>
  );
}

export default App;