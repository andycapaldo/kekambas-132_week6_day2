from app import app
from flask import render_template, redirect, url_for
from app.forms import Phonebook



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/phonebook', methods=['GET', 'POST'])
def phonebook():
    phonebook = Phonebook()
    if phonebook.validate_on_submit():
        first_name = phonebook.first_name.data
        last_name = phonebook.last_name.data
        phone_number = phonebook.phone_number.data
        address = phonebook.address.data
        print(first_name, last_name, phone_number, address)

        return redirect(url_for('index'))
    return render_template('phonebook.html', phonebook=phonebook)