from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Define the route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        email_addresses = extract_email_addresses(text)
        unique_emails = remove_duplicates(email_addresses)
        save_emails(unique_emails)
        return render_template('result.html', emails_line_by_line='\n'.join(unique_emails), emails_single_line=';'.join(unique_emails))
    return render_template('index.html')

# Function to extract email addresses from the text
def extract_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

# Function to remove duplicate email addresses
def remove_duplicates(email_list):
    return list(set(email_list))

# Function to save the email addresses to a file
def save_emails(email_list):
    with open('emails.txt', 'w') as file:
        for email in email_list:
            file.write(email + '\n')

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)