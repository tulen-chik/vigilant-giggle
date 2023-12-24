from flask import Flask, render_template, url_for, request, redirect, abort
from .database import db, Users, Catalog, ItemsBought
from os import chdir

def findex():
    if request.method == 'POST':
        if request.form['search']:
            id = request.form['search']
            return redirect(url_for('catalog', id=id))
    print(Users.query.all())
    return render_template(chdir('../templates/index.html'), title='главная страница')