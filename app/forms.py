from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length


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