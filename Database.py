from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Builtins(db.Model):
    __tablename__ = 'builtins'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Decks %r>' % self.description

    def get_description(self):
        return self.description

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Decks(db.Model):
    __tablename__ = 'decks'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Decks %r>' % self.description

    def get_description(self):
        return self.description

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Kitchens(db.Model):
    __tablename__ = 'kitchens'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Kitchens %r>' % self.description

    def get_description(self):
        return self.description

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo
