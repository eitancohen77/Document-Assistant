import React, { useState } from 'react'

function DataManipulationPage() {

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
        <>
      <div class="jumbotron text-center">
        <h1>AI Assistant 🤖</h1>
      </div>
      <div class="container p-4 my-4 border">

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder='Enter your question'
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button class="btn-primary btn block" type="submit">Submit</button>
        </form>
        <p>AI Response
          <div class="container p-4">{result} </div>
        </p>
      </div>
      <div class="container">
        <footer class="py-3 my-4">
          <ul class="nav pb-3 mb-3">
            <li>
              <a class="nav-link px-2 text-body-secondary" href="/chroma">~Chroma~</a>
            </li>
            <li>
              <a class="nav-link px-2 text-body-secondary" href="/chromaAll">~ChromaAll~</a>
            </li>
          </ul>
        </footer>
      </div>
    </>
    );
}

export default DataManipulationPage;