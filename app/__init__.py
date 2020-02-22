from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PRO8LEMS3W%LLArr1458ES7rnG'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)
csrf.init_app(app)
from app import views
