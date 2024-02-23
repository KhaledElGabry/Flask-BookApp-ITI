
from flask import Blueprint

book_blueprint = Blueprint("books",__name__,url_prefix="/" )

from books import views
from books import api_views