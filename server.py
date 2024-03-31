from flask import Flask, render_template, request

app = Flask(__name__)

# Define route to serve HTML page
@app.route('http://localhost:5000/')
def index():
    return render_template('index.html')

# Define route to handle AJAX request
@app.route('/execute_code', methods=['POST'])
def execute_code():
    # Retrieve data from request (if needed)
    data = request.get_json()

    # Execute Python code (replace this with your actual code)
    result = {'output': 'Python code executed successfully'}
    
    # Return result as JSON
    return result

if __name__ == '__main__':
    app.run(debug=True)
