

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addtaskform(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    submit=SubmitField('Submit')

class deletetaskform(FlaskForm):
    
    submit=SubmitField('Delete')        