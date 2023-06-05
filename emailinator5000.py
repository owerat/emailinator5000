from flask import Flask, render_template, request
import re

app = Flask(__name__)

# route for homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        email_addresses = extract_email_addresses(text)
        unique_emails = remove_duplicates(email_addresses)
        save_emails(unique_emails)
        return render_template('result.html', email_list=unique_emails)
    return render_template('index.html')

# extract email addresses 
def extract_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

# remove dupes
def remove_duplicates(email_list):
    return list(set(email_list))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
