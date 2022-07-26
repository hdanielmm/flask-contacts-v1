from flask import Blueprint, jsonify, redirect, render_template, request, url_for, flash
from utils.db import db, ma
from models.contact import Contacts, ContactsSchema

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    contacts = Contacts.query.all()
    contact_schema = ContactsSchema(many=True)
    response = contact_schema.dump(contacts)
    print(response)
    # return jsonify({'response', response})
    # return render_template('index.html', contacts=contacts)
    return jsonify({'response': response})

@contacts.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        contact = Contacts(fullname, phone, email)

        db.session.add(contact)
        db.session.commit()

        flash('Contact added successfully')
        
        return redirect(url_for('contacts.index'))
        

@contacts.route('/edit/<id>')
def get_contact(id):
    contact = Contacts.query.get(id)
    
    return render_template('edit-contact.html', contact=contact)

@contacts.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        contact = Contacts.query.get(id)
        
        contact.fullname = request.form['fullname']
        contact.phone = request.form['phone']
        contact.email = request.form['email']

        db.session.commit()
    
        flash('Contact updated successfully')
        return redirect(url_for('contacts.index'))

@contacts.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contacts.query.get(id)
    
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully')
    
    return redirect(url_for('contacts.index'))