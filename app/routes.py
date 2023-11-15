from app import app, db
from app.models import User, Income, Expense
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, IncomeForm, ExpenseForm


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@app.route('/landing')
def landing():
    """Landing URL"""
    return render_template('landing.html', title='Index Page')




@app.route('/login', methods=['GET', 'POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect (url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {form.email.data}')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered successfuly. Login to continue')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    

@app.route('/home')
@login_required
def home():
    """Home URL"""
    incomes =Income.query.all()
    expenses = Expense.query.all()
    return render_template('home.html', title='Your Financial Health', incomes=incomes, expenses=expenses)


@app.route('/income', methods=['GET', 'POST'])
def income():
    """Landing URL"""
    form = IncomeForm()
    if form.validate_on_submit():
        income = Income(
            source = form.source.data,
            amount = form.amount.data,
            author = current_user
        )
        db.session.add(income)
        db.session.commit()
        flash('Income saved')
        return redirect(url_for('income'))
    incomes = Income.query.all()
    return render_template('income.html', title='Income', form=form, incomes=incomes)


@app.route('/expense', methods=['GET', 'POST'])
def expense():
    """Landing URL"""
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(
            item = form.item.data,
            amount = form.amount.data,
            author = current_user
        )
        db.session.add(expense)
        db.session.commit()
        flash('Expense saved')
        return redirect(url_for('expense'))
    expenses = Expense.query.all()
    return render_template('expense.html', title='Expense', form=form, expenses=expenses)

@app.route('/expense/<int:id>', methods=['GET', 'POST'])
def expenseitem(id):
    expense = Expense.query.filter_by(id=id).first()
    db.session.delete(expense)
    db.session.commit()
    flash(f'Expense {expense.item} has been deleted successfuly')
    return redirect(url_for('expense'))

@app.route('/income/<int:id>', methods=['GET', 'POST'])
def incomesource(id):
    income = Income.query.filter_by(id=id).first()
    db.session.delete(income)
    db.session.commit()
    flash(f'Income {income.source} has been deleted successfuly')
    return redirect(url_for('income'))