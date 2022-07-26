from flask import Flask, flash, jsonify, render_template, request, url_for, redirect
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from routes.contacts import contacts
from config import DATABASE_CONNECTION_URI, SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = SECRET_KEY

SQLAlchemy(app)
Marshmallow(app)

app.register_blueprint(contacts)