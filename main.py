from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('User.username'))
    addresses = db.relationship('Address', backref='person', lazy=True)


class Address(db.Model):
    __tablename__ = 'Address'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
