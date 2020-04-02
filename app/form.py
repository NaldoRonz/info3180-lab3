from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, Length

class ContactForm(FlaskForm):
    Firstname = StringField("Firstname", validators = [DataRequired(), Length(min=2, max =20), Regexp("^[ a-zA-Z]+$")])
    Lastname = StringField("Lastname", validators = [DataRequired(), Length(min=2, max =20), Regexp("^[ a-zA-Z]+$")])
    Email = StringField("Email", validators = [DataRequired(),Email(),])
    Subject = StringField("Subject", validators = [DataRequired(), Length(max =20)])
    your_message = TextAreaField("Message", validators = [DataRequired(), Length(max =500)])
