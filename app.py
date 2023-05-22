from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from configs import secret_key
from messages import messages
import utils

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

messages = messages
users = {}

# Test route
@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello, world!'})

@app.route('/')
def home():
    return render_template('index.html', messages=messages)


@app.route('/new_user/', methods=('GET', 'POST'))
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        utils.create_user(name, phone, email)

    return render_template('new_user.html')

@app.route('/incoming', methods=['POST'])
def store_data():
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        # Handle form data
        data = dict(request.form)
        with open('incoming.txt', 'a') as f:
            f.write(str(data))
            f.write('\n')
            f.write('\n')
        # Here we can parse the incoming information and create variables such as "sender's phone number", conversation, etc
        # Based off the incoming number + the registration information in this app, it will determine whose Square API will be called
        ## Registration information will have to map <user phone number> to <user square api account>
        ## This function will do a lookup in the above mapping to determine where to send sq api reqs
        ## SQLite here or just a text/csv file for now?
        return 'Form data stored successfully!'
    else:
        print('Unsupported media type - must be application/x-www-form-urlencoded')
        return 'Unsupported media type - must be application/x-www-form-urlencoded'

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)
