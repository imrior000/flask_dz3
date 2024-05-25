from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    passwd = PasswordField('passwd', validators=[DataRequired(), Length(min=8)])
    passwd2 = PasswordField('passwd2', validators=[DataRequired(), Length(min=8), EqualTo('passwd')])
