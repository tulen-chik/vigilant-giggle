from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Catalog(db.Model):
    __tablename__ = 'catalog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    description = db.Column(db.Text)

    def __repr__(self) -> str:
        return f'<catalog_item {self.id}>'
    
class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(500))

class ItemsBought(db.Model):
    __tablename__ = 'items'

    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    id_items = db.Column(db.Integer, db.ForeignKey('catalog.id'))
