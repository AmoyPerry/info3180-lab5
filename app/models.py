# Add any model classes for Flask-SQLAlchemy here
from . import db 


class MovieModel(db.Model):
    __tablename__ = "movies"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(200))
    poster = db.Column(db.String(80))
    create_at = db.Column(db.DateTime())
    