from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://coralite:BlKgDrSm9600!@68.178.217.6/coralite'
db = SQLAlchemy(app)


class Kitchen(db.Model):
    __tablename__ = 'kitchens'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description')
    galleryId = db.Column('galleryId')
    cpo = db.Column('cpo')

    def __init__(self, description, galleryId, cpo):
        self.description = description
        self.galleryId = galleryId
        self.cpo = cpo

    def __repr__(self):
        return '<Gallery %r>' % self.description

    def get_description(self):
        return self.description

    def get_galleryId(self):
        return self.galleryId

    def get_cpo(self):
        return self.cpo
