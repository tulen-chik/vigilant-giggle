from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form['search']
        return redirect(url_for('catalog', id=id))
    return render_template('index.html')


@app.route('/catalog/<int:id>', methods=['GET', 'POST'])
def catalog(id):
    if request.method == 'POST':
        id = request.form['search']
        return redirect(url_for('catalog', id=id))
    return render_template('catalog.html', id=id)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 