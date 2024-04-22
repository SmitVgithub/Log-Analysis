from flask import Flask, render_template, request
import os
import logging
import sys

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and perform log analysis
@app.route('/greet', methods=['POST'])
def greet():
    # Capture form data
    name = request.form['name']

    # Check if the entered value is a number
    if not name.isalpha():
        # Log the error
        logging.error(f"User entered a name with non-alphabetic characters: {name}")

        # Render template with error message
        return render_template('error.html', error_message="Please enter a valid name with alphabetic characters only.")

    # Log the user's valid name
    logging.info(f"User entered a valid name: {name}")

    # Perform log analysis
    analysis_result = perform_log_analysis(name)

    # Render template with analysis result
    return render_template('greet.html', name=name, analysis_result=analysis_result)

def perform_log_analysis(name):
    # Perform log analysis based on the name submitted in the form
    # For demonstration, let's count occurrences of the name in a log file
    log_file = 'app.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            log_content = file.read()
        name_count = log_content.count(name)
        return f"Occurrences of '{name}' in log file: {name_count}"
    else:
        return "Log file not found."

if __name__ == '__main__':
    app.run(debug=True)
    