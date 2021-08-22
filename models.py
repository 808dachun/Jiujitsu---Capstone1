"""Models for juijitsu  app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


DEFAULT_IMAGE = "https://cdn.shopify.com/s/files/1/1800/2299/articles/4_1024x1024.jpg?v=1607405733"


class phase(db.Model):
    """Phase."""

    __tablename__ = "phase"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    imageCredit = db.Column(db.Text, nullable=False)

class ground_position(db.Model):
    """Phase."""

    __tablename__ = "ground_position"

    groundPositionCode = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    imageCredit = db.Column(db.Text, nullable=False)

class move(db.Model):
    """moves"""

    __tablename__ = "move"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    groundPositionCode = db.Column(db.Text, db.ForeignKey('ground_position.groundPositionCode'))
    imageCredit = db.Column(db.Text, nullable=False)

    gpc = db.relationship('ground_position', backref = 'move')

class standing(db.Model):
    """Phase."""

    __tablename__ = "standing"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    imageCredit = db.Column(db.Text, nullable=False)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)