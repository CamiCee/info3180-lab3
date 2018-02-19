from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']= 'hot potatoes'
app.config['MAIL_SERVER']= 'smtp.mailtrap.io'
app.config['MAIL_PORT']= '2525'
app.config['MAIL_USERNAME']= 'fa7d0625113049'
app.config['MAIL_PASSWORD']= '0623d337bf6c72'

mail=Mail(app)
from app import views