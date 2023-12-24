from flask import Flask, render_template, url_for, request, redirect, abort
from Nord.database import db, Users, Catalog, ItemsBought

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.app_context().push()

db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['search']:
            id = request.form['search']
            return redirect(url_for('catalog', id=id))
    print(Users.query.all())
    return render_template('index.html', title='главная страница')


@app.route('/catalog/<id>', methods=['GET', 'POST'])
def catalog(id):
    if request.method == 'POST':
        if request.form['search']:
            id = request.form['search']
            return redirect(url_for('catalog', id=id))
    
    data = Catalog.query.filter(Catalog.name == id).first()
    if not data:
        abort(404)

    return render_template('catalog.html', data=data, title='страница каталога')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['search']:
            id = request.form['search']
            return redirect(url_for('catalog', id=id))
    return render_template('login.html', title='войти')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='страница не найдена')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
