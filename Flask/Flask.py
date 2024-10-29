from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello_1')
def hello_1():
    text = 'Привет 1'
    return render_template('Hello_1.html', text=text)


@app.route('/hello_2')
def hello_2():
    text_1 = 'Привет 2'
    text_2 = 'Привет 3'
    return render_template('Hello_2.html', text_1=text_1, text_2=text_2)


if __name__ == '__main__':
    app.run()