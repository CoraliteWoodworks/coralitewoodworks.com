from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Additions(db.Model):
    __tablename__ = 'additions'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Additions %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Bars(db.Model):
    __tablename__ = 'bars'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Bars %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Basements(db.Model):
    __tablename__ = 'basements'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Basements %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Bathrooms(db.Model):
    __tablename__ = 'bathrooms'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Bathrooms %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


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
        return '<Builtins %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

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
        if self.description is not None:
            return self.description
        else:
            return ""

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
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Mantels(db.Model):
    __tablename__ = 'mantels'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Mantels %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Mudrooms(db.Model):
    __tablename__ = 'mudrooms'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Mudrooms %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Offices(db.Model):
    __tablename__ = 'offices'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Offices %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Paneling(db.Model):
    __tablename__ = 'paneling'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Paneling %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Stock %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo


class TV(db.Model):
    __tablename__ = 'tv'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(length=256))
    gallery_id = db.Column('gallery_id', db.String(length=512))
    cpo = db.Column('cpo', db.String(length=256))

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<TV %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_gallery_id(self):
        return self.gallery_id

    def get_cpo(self):
        return self.cpo
