from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    post = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comments', validators = [Required()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    