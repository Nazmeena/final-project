# Links the database with your routes, by creating input forms. 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField

from application.models import Students, Classes

class StudentForm(FlaskForm):
    name = StringField("Name")
    position = StringField("Position")
    fk_classid = IntegerField("Class ID")
    submit = SubmitField("Submit")

class ClassForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")
