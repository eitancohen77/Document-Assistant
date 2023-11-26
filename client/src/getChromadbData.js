import React, { useState, useEffect } from 'react'

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
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                />
                <button type="submit">Submit</button>
            </form>
            <p>ChromaDB Documents: {result.documents && result.documents.join(', ')}</p>
        </div>
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
        <div>
            <p>{data.documents}</p>
        </div>
    );
}
