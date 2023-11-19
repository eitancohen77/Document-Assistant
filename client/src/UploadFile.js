import React from 'react'
import { useState } from 'react'

function UploadFile() {
    const [file, setFile] = useState();

    function handleFile(e) {
        setFile(e.target.files[0]);
        console.log(e.target.files[0]);
    }

    function handleUPoad() {
        const formData = new FormData();
        formData.append('file', file);
        fetch(
            'url',
            {
                method: "POST",
                body: formData
            }

        ).then((response) => response.json())
            .then(
                (result) => {
                    console.log('success', result)
                }
            )
            .catch(error => {
                console.error("Error: ", error)
            })
    }

    return (
        <div>
            <p>Upload File</p>
            <form>
                <input type="file" name="file" onChange={handleFile} />
                <button>Upload File</button>
            </form>
        </div>
    )
}

export default UploadFile;