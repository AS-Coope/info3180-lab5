from . import db

class Movies(db.Model):

    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    poster = db.Column(db.String(200))
    date_created = db.Column(db.DateTime)

    def __init__(self, title, description, poster, date_created):
        self.title = title
        self.description = description
        self.poster = poster
        self.date_created = date_created
