from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    id = IntegerField('Task id')
    name = StringField('Task Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    full_text = TextAreaField('Full text')
    is_important = BooleanField('Is Important?')
    status = BooleanField('Status')
    submit = SubmitField('Create Task')
