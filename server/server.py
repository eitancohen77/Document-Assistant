from flask import Flask, jsonify, request
from flask_cors import CORS
import langchain_helper as lch
import chromadb
import json

chroma_client = chromadb.Client()
app = Flask(__name__)
CORS(app)

collection = chroma_client.create_collection(name="my_collection")
id = 0

@app.route("/manipulateData", methods=['GET', 'POST'])
def manipulateData():
    global id
    if request.method == 'POST':

        # Pull Data out
        data = request.json
        user_input = data['userInput']

        # Prompt intelligent model to ask based on input.
        processed_data = lch.generate_output(user_input)['output']
        id = id + 1

        # Try indexing??
        data_to_store = json.dumps({'input': user_input, 'output': processed_data})
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

    if (request.method == "POST"):

        try:
            print("WENT THROUGHHHH")
            if request.method == "POST":
                data = request.json
                user_input = data['userInput']

                results = collection.query(
                    query_texts = [user_input],
                    n_results=1,
                    include=['distances', 'metadatas', 'documents']
                )

                document = (results['documents'][0])  
                print("Type of document:", type(document))

                print(document)
                objectData = json.loads(document[0])
                print(objectData)

                return jsonify({"processedData": objectData['output']})
            return
        
        except Exception as e:
            print("An error occurred:", e)
            return jsonify({"error": str(e)})


@app.route("/getAllChromaDBData", methods=['GET', 'POST'])
def getAllChromaDBData():
    results = collection.get()
    return jsonify({"allData": results})

if __name__ == "__main__":
    app.run(debug=True)