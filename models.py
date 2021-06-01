from . import db
from flask_login import UserMixin


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    middleInitial = db.Column(db.String(1))
    lastName = db.Column(db.String(150))
    birthDate = db.Column(db.String(50))
    address = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phoneNumber = db.Column(db.String(150))
    emergencyContactFirstName = db.Column(db.String(150))
    emergencyContactLastName = db.Column(db.String(150))
    emergencyContactPhoneNumber = db.Column(db.String(150))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    accounts = db.relationship('Account')
