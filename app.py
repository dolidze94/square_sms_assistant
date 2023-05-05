from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from configs import secret_key
from messages import messages

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

messages = messages

# Test route
@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello, world!'})

@app.route('/')
def home():
    return render_template('index.html', messages=messages)


@app.route('/entry/', methods=('GET', 'POST'))
def entry():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('home'))

    return render_template('entry.html')

@app.route('/incoming', methods=['POST'])
def store_data():
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        # Handle form data
        data = dict(request.form)
        with open('incoming.txt', 'a') as f:
            f.write(str(data))
            f.write('\n')
            f.write('\n')
        print('Form data stored successfully!')
    else:
        print('Unsupported media type - must be application/x-www-form-urlencoded')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)
