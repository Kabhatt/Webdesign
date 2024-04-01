from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_code', methods=['POST'])
def execute_code():
    if request.method == 'POST':
        # Extract data from the request
        data = request.get_json()
        # Process the data (e.g., execute the provided code)
        result = process_data(data)
        # Return a JSON response
        return jsonify(result)
    else:
        # Handle other HTTP methods (e.g., GET) if needed
        return 'Method Not Allowed', 405

def process_data(data):
    # Example function to process the data (replace with your logic)
    code = data.get('code')
    # Execute the code and return the result
    result = eval(code)
    return {'result': result}

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
