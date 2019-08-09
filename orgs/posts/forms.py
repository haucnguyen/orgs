from flask_wtf import FlaskForm
from datetime import date
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Event Name', validators=[DataRequired()])
    date = DateField('Event date', default=date.today(), format='%m/%d/%Y', validators=[DataRequired(message="You need to enter the date.")])
    location = StringField('Location', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create Event')
