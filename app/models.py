from . import db

class Movies(db.Model):

    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    poster = db.Column(db.String(200))
    date_created = db.Column(db.DateTime)
