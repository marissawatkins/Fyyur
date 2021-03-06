from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
import datetime


app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/todo'

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String)
    shows = db.relationship('Show', backref='Venue', lazy=True)




class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue= db.Column(db.Boolean)
    seeking_description = db.Column(db.String)
    shows = db.relationship('Show', backref='Artist', lazy=True)



class Show(db.Model):
  _tablename__ = 'Show'
  show_id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime())
  '''create relationships between show and Artist, Venue'''
  artist_id = db.Column(db.Integer, db.ForeignKey(Artist.id), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey(Venue.id), nullable=False)
