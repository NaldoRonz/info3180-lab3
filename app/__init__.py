from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PROBLEMS3'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'c70a8ece552378'
app.config['MAIL_PASSWORD'] = '6633c1dfb447e2'

mail = Mail(app)
from app import views
