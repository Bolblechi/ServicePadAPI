from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(330), unique=True)
    password = db.Column(db.String(100))
    fullname = db.Column(db.String(1000))
    photo = db.Column(db.LargeBinary)
