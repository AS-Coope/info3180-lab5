from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Provide a brief description of the movie submitted:', validators=[InputRequired()])
    poster = FileField(
        'Movie Poster', validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
        ]
    )