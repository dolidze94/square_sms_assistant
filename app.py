from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)
