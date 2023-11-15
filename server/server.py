from flask import Flask, jsonify, request
from flask_cors import CORS
import langchain_helper as lch

app = Flask(__name__)
CORS(app)


@app.route("/manipulateData", methods=['GET', 'POST'])
def manipulateData():
    if request.method == 'POST':

        # Extract data from post request
        data = request.json
        user_input = data['userInput']

        # Process the data (example: reverse the string)
        processed_data = lch.generate_output(user_input)['output']

        # Return the processed data
        return jsonify({"processedData": processed_data})
    return 
    
if __name__ == "__main__":
    app.run(debug=True)