from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Account
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        middleInitial = request.form.get('middleInitial')
        lastName = request.form.get('lastName')
        birthDate = request.form.get('birthDate')
        address = request.form.get('address')
        email = request.form.get('email')
        phoneNumber = request.form.get('phoneNumber')
        emergencyContactFirstName = request.form.get('emergencyContactFirstName')
        emergencyContactLastName = request.form.get('emergencyContactLastName')
        emergencyContactPhoneNumber = request.form.get('emergencyContactPhoneNumber')

        if len(firstName) < 0:
            flash('Account not finished', category='error')
        elif len(middleInitial) < 0:
            flash('Account not finished', category='error')
        elif len(lastName) < 0:
            flash('Account not finished', category='error')
        elif len(birthDate) < 0:
            flash('Account not finished', category='error')
        elif len(email) < 0:
            flash('Account not finished', category='error')
        elif len(address) < 0:
            flash('Account not finished', category='error')
        elif len(emergencyContactFirstName) < 0:
            flash('Account not finished', category='error')
        elif len(emergencyContactLastName) < 0:
            flash('Account not finished', category='error')
        elif len(emergencyContactPhoneNumber) < 0:
            flash('Account not finished', category='error')
        else:
            new_account = Account(firstName=firstName, middleInitial=middleInitial, lastName=lastName, birthDate=birthDate, address=address, email=email, phoneNumber=phoneNumber, emergencyContactFirstName=emergencyContactFirstName, emergencyContactLastName=emergencyContactLastName, emergencyContactPhoneNumber=emergencyContactPhoneNumber, admin_id=current_user.id)
            db.session.add(new_account)
            db.session.commit()
            flash('Account added!', category='success')

    return render_template("home.html", admin=current_user)


@views.route('/delete-account', methods=['POST'])
def delete_account():
    account = json.loads(request.data)
    accountId = account['accountId']
    account = Account.query.get(accountId)
    if account:
        if account.admin_id == current_user.id:
            db.session.delete(account)
            db.session.commit()

    return jsonify({})