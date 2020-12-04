from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from wtforms.validators import Email
from wtforms.validators import Length 
from wtforms.validators import EqualTo
from app.models import User
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    remember_me = BooleanField('Remember Me')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  
        if user is None or not user.check_password(password=password.data):
            raise ValidationError('Username or password incorrect.')
    
#     def validate_password(self, password):
#     user = User.query.filter_by(username=username.data).first()
#     if not user.check_password(password.data):
#         raise ValidationError("Incorrect Password")
            
            
             
                        


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15) ])
    email = StringField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80) ])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]) 
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username taken.') 
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address already used.') 
