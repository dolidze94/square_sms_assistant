from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from configs import secret_key
from messages import messages
import utils
import sys
#Debug
import traceback

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
def incoming():
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        # Handle form data
        data = dict(request.form)
        try:
            incoming_result = utils.incoming_processor(data)
            with open('incoming.txt', 'a') as f:
                f.write(str(data))
                f.write(str(incoming_result))
                f.write('\n')
                f.write('\n')
            return "Successfully processed incoming text: " + incoming_result
        except Exception as e:
            tb = traceback.print_exception(e)#debug
            print('Unable to process incoming result. Error:\n %s' % str(e), file=sys.stderr)#debug
            return "Error encountered when processing incoming data: " + str(e)

    else:
        print('Unsupported media type - must be application/x-www-form-urlencoded')
        return 'Unsupported media type - must be application/x-www-form-urlencoded'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    #app.run(host='0.0.0.0',port=5000)