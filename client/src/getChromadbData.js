import React, { useState, useEffect } from 'react'
import { NavLink } from 'react-router-dom';

export function ChromaDBData() {

    const [input, setInput] = useState('')
    const [result, setResult] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch("http://127.0.0.1:5000/getChromaDBData", {
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
            <nav className="navbar navbar-expand-sm navbar-light bg-light shadow mb-3">
        <div className="container-fluid">
          <nav>
            <ul className="navbar-nav me-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/">
                  Home
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/chromaAll">
                  ChromaAll
                </NavLink>
              </li>
            </ul>
          </nav>
        </div>
      </nav>
            <div class="container p-4 my-4 border">
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                    />
                    <button class="btn-primary btn block" type="submit">Submit</button>
                </form>
                <p>ChromaDB Documents: {result.documents && result.documents.join(', ')}</p>
            </div>
        </>
    );
}

export function ChromaDBDataDisplay() {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://127.0.0.1:5000/getAllChromaDBData");
                if (response.ok) {
                    const jsonResponse = await response.json();
                    setData(jsonResponse.allData);
                }
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        fetchData();
    }, []);

    return (
        <>
            <div class="jumbotron text-center">
                <h1>AI Assistant 🤖</h1>
            </div>
            <div>
                <p>{data.documents}</p>
            </div>
        </>
    );
}
