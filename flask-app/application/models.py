# How your databases are going to look. 
from application import db 

class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    position = db.Column(db.String(30))
    fk_classid = db.Column(db.Integer, db.ForeignKey('classes.id'))
