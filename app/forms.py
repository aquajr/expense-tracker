from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    '''Login Form'''
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    '''Register Form'''
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    register = SubmitField('Register')

    def validate_email(self, email):
        '''Validate new  email'''
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')

class IncomeForm(FlaskForm):
    '''Income Form'''
    source = StringField('Source', validators=[DataRequired(), Length(1, 64)])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add')

class ExpenseForm(FlaskForm):
    '''Expense Form'''
    item = StringField('Item', validators=[DataRequired(), Length(1, 64)])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')