from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import  QuerySelectField
from models import Category

class BookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    NumberPage = IntegerField('Number of Pages', validators=[DataRequired()])
    image = StringField('Image URL')
    category_id = QuerySelectField("Category", query_factory=lambda:Category.get_all_categories())
