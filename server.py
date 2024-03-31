from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Define route to serve project1.html
@app.route('/')
def project():
    return render_template('project1.html')

# Define route to handle AJAX request for executing Python code
@app.route('/execute_code', methods=['POST'])
def execute_code():
    try:
        # Execute the Python code from baye.py
        result = subprocess.run(['python', 'baye.py'], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr

        # If there was an error, return the error message
        if error:
            return jsonify({'output': error})

        # Return the output of Python code execution
        return jsonify({'output': output})
    except Exception as e:
        # Return the exception message if an error occurred
        return jsonify({'output': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
