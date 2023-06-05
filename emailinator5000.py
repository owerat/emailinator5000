from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    emails_line_by_line = ""
    emails_single_line = ""
    if request.method == 'POST':
        text = request.form['text']
        email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        emails = re.findall(email_pattern, text)
        
        with open('emails.txt', 'w') as f:
            for email in emails:
                f.write(email + "\n")

        emails_line_by_line = "\n".join(emails)
        emails_single_line = "; ".join(emails)
        
    return render_template('index.html', emails_line_by_line=emails_line_by_line, emails_single_line=emails_single_line)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
