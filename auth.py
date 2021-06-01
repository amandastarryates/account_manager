from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        admin = Admin.query.filter_by(username=username).first()
        if admin:
            if check_password_hash(admin.password, password):
                flash('Logged in successfully', category='success')
                login_user(admin, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Username does not exist. Please create account', category='error')
    return render_template("login.html", admin=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        admin = Admin.query.filter_by(username=username).first()
        if admin:
            flash('Username already exists', category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be at least 2 characters.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be at least 2 characters.', category='error')
        elif len(username) < 5:
            flash('Username must be at least 5 characters.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            new_admin = Admin(firstName=firstName, lastName=lastName, email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_admin)
            db.session.commit()
            login_user(new_admin, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("register.html", admin=current_user)