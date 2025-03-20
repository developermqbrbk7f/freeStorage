from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

PASSWORD_FILE = 'passwords.json'

def load_passwords():
    try:
        with open(PASSWORD_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f, indent=4)

@app.route('/')
def index():
    passwords = load_passwords()
    return render_template('index.html', passwords=passwords)

    # new features soon

if __name__ == '__main__':
    app.run(debug=True)
