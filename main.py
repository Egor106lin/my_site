from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {

    }
    return render_template('index.html', **context)


@app.route('/top1')
def top1():
    return render_template('top1.html')


if __name__ == '__main__':
    app.run()
