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


@app.route('/top2')
def top2():
    return render_template('top2.html')


@app.route('/top3')
def top3():
    return render_template('top3.html')


@app.route('/top4')
def top4():
    return render_template('top4.html')


@app.route('/top5')
def top5():
    return render_template('top5.html')


@app.route('/top6')
def top6():
    return render_template('top6.html')


@app.route('/top7')
def top7():
    return render_template('top7.html')


@app.route('/top8')
def top8():
    return render_template('top8.html')


@app.route('/top9')
def top9():
    return render_template('top9.html')


@app.route('/top10')
def top10():
    return render_template('top10.html')


if __name__ == '__main__':
    app.run()
