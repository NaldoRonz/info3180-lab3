from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    first_name = StringField("Firstname", validators = [DataRequired()])
    last_name = StringField("Lastname", validators = [DataRequired()])
    my_email = StringField("Email", validators = [DataRequired(),Email()])
    my_subject = StringField("Subject", validators = [DataRequired()])
    my_message = StringField("Message", validators = [DataRequired()])
