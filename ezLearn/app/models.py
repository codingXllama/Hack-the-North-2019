# Insert Stuff to do with Models
from flask_sqlalchemy import SQLAlchemy

from app import app  # Change this based on the application

db = SQLAlchemy(app)


class account(db.Model):
    username = db.Column(db.String(48), unique=True)
    full_name = db.Column(db.String(128))
    password = db.Column(db.String(64))
    account_id = db.Column(db.String(24))
    # Maybe add names and more personal stuff later


class image(db.Model):
    path = db.Column(db.String(200))
    name = db.Column(db.String(64))
    crop_height = db.Column(db.Integer())
    crop_width = db.Column(db.Integer())
    offset_x = db.Column(db.Integer())
    offset_y = db.Column(db.Integer())


class document(db.Model):
    path = db.Column(db.String(200))
    name = db.Column(db.String(64))


class duo(db.Model):  # This is a db entry for pairs of question and answers in a highlighted document
    question = db.Column(db.String(400))
    answer = db.Column(db.String(400))
    duo_id = db.Column(db.String(64))
