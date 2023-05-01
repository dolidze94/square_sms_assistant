from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from configs import secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

# Test route
@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello, world!'})

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/entry/', methods=('GET', 'POST'))
def create():
    return render_template('entry.html')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=5000)
