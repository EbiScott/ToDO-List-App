import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login/')
def login():
    return url_for('login.html')


@app.route('/login/<:id>/', methods=['POST', 'GET'])
def loginWithId(id):
    if methods == 'POST':
        username = request.form.get('id')

if __name__ == "__main__":
    app.run(debug=True)