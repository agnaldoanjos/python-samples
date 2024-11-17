from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    born_date = db.Column(db.String(10), nullable=False)
    document = db.Column(db.String(15), unique=True, nullable=False)
