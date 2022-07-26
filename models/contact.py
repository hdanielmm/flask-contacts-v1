from utils.db import db, ma

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    def __init__(self, fullname, phone, email):
        self.fullname = fullname
        self.phone = phone
        self.email = email

    # def __repr__(self):
    #     return f'fullname: {self.fullname}, phone: {self.phone}, email: {self.email}'

class ContactsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contacts