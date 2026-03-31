from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, bcrypt  # Готовые объекты
from app.models import User
from app.forms import LoginForm, RegistrationForm

@app.route('/')  # Обычные декораторы @app.route
@login_required
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed)
        db.session.add(user); db.session.commit()
        flash('Зарегистрирован!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user); return redirect(url_for('index'))
        flash('Ошибка входа', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user(); return redirect(url_for('login'))

@app.route('/click')
@login_required
def click():
    current_user.clicks += 1; db.session.commit()
    return redirect(url_for('index'))