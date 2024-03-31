from flask import Flask, render_template, request

app = Flask(__name__)

# Define route to serve project1.html
@app.route('/')
def project():
    return render_template('project1.html')

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
