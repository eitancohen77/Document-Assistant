from flask import Flask, jsonify, request
from flask_cors import CORS
import langchain_helper as lch
import chromadb

chroma_client = chromadb.Client()
app = Flask(__name__)
CORS(app)

collection = chroma_client.create_collection(name="my_collection")
id = 0

@app.route("/manipulateData", methods=['GET', 'POST'])
def manipulateData():
    global id
    if request.method == 'POST':

        # Extract data from post request
        data = request.json
        user_input = data['userInput']

        # Process the data (example: reverse the string)
        processed_data = lch.generate_output(user_input)['output']
        id = id + 1

        data_to_store = "INPUT: " + user_input + ". OUTPUT: " + processed_data
        collection.add(
            documents=[data_to_store],
            metadatas={"source": "my_source"},
            ids=[str(id)]
        )

        # Return the processed data
        return jsonify({"processedData": processed_data})
    return 

@app.route("/getChromaDBData", methods=['GET', 'POST'])
def getChromaDBData(): 
    if request.method == "POST":
        data = request.json
        user_input = data['userInput']

        results = collection.query(
            query_texts = [user_input],
            n_results=2,
            include=['distances', 'metadatas', 'documents']
        )
        return jsonify({"processedData": results})
    return

@app.route("/getAllChromaDBData", methods=['GET', 'POST'])
def getAllChromaDBData():
    results = collection.get()
    return jsonify({"allData": results})

if __name__ == "__main__":
    app.run(debug=True)