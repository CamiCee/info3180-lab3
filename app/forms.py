from flask_wtf import Form 
from wtforms.fields import TextField, TextAreaField
from wtforms.validators import DataRequired, Email

class MyForm(Form):
    name=TextField('Name', validators=[DataRequired()])
    subject=TextField('Subject' , validators=[DataRequired()])
    email=TextField('Email', validators=[DataRequired(), Email()])
    message=TextAreaField('Message', validators=[DataRequired()])
    
    
    

