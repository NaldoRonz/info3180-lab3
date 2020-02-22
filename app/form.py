from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    Firstname = StringField("Firstname", validators = [DataRequired()])
    Lastname = StringField("Lastname", validators = [DataRequired()])
    Email = StringField("Email", validators = [DataRequired(),Email()])
    Subject = StringField("Subject", validators = [DataRequired()])
    your_message = StringField("Message")
