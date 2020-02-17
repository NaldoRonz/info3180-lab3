from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    FirstName = StringField("FirstName", validators = [DataRequired()])
    LastName = StringField("LastName", validators = [DataRequired()])
    Email = StringField("Email", validators = [DataRequired(),Email()])
    Subject = StringField("Subject", validators = [DataRequired()])
    Message = StringField("Message", validators = [DataRequired()])
