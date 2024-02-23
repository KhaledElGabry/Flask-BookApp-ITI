# define parser to convert request.data to python datatypes

from flask_restful import reqparse

books_parser = reqparse.RequestParser()
books_parser.add_argument('name', type=str, required=True, help="Name is required")
books_parser.add_argument('image', type=str)
books_parser.add_argument('price',type=int)
books_parser.add_argument('NumberPage', type=int)
books_parser.add_argument('category_id', type=int)