from flask import Flask, jsonify, request
from flask_cors import CORS
import langchain_helper as lch
import langchain_doc_assist as lchd

app = Flask(__name__)
CORS(app)


@app.route("/manipulateData", methods=['GET', 'POST'])
def manipulateData():
    if request.method == 'POST':
        print("POST request")
        # Extract data from post request
        data = request.json
        user_input = data['userInput']

        # Process the data (example: reverse the string)
        processed_data = lch.generate_output(user_input)['output']

        # Return the processed data
        return jsonify({"processedData": processed_data})
    return 
    
@app.route("/doc", methods=['POST'])
def docAssist():
    query = request.form['query']
    file = request.form['file']

    if file == None:
        return "Missing file"
    if query == None:
        return "Missing query"
    
    result = lchd.doc_assist(file, query)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)