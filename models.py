import os
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

class Actor(db.Model):
  __tablename__ = 'actors'

  id = Column(db.Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(db.Integer, nullable=False)
  gender = Column(String, nullable=False)

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }

class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(db.Integer, primary_key=True)
  title = Column(String, nullable=False)
  release_date = Column(db.DateTime, nullable=False)

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date
      }
