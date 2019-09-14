from flask_sqlalchemy import SQLAlchemy

from app import app #Change this based on the application

db = SQLAlchemy(app)

class account(db.Model):
    db.Column('id', db.Integer, primary_key=True)
    db.Column('username', db.String(48))
    db.Column('password', db.String(64))
    db.Column('account_id', db.String(24))
    # Maybe add names and more personal stuff later

class image(db.Model):
    db.Column('path', db.String(200))
    db.Column('name', db.String(64))
    db.Column('crop_height', db.Integer())
    db.Column('crop_width', db.Integer())
    db.Column('offset_x', db.Integer())
    db.Column('offset_y', db.Integer())

class document(db.Model):
    db.Column('path', db.String(200))
    db.Column('name', db.String(64))

class duo(db.Model): #This is a db entry for pairs of question and answers in a highlighted document
    db.Column('question', db.String(400))
    db.Column('answer', db.String(400))
    db.Column('duo_id', db.String(64))
