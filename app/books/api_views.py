from flask_restful import Resource, fields, marshal_with
from flask import request
from models import Book, db
from books import book_blueprint
from books.parsers import  books_parser

@book_blueprint.route("/api", endpoint="api")
def get_book():
    books = Book.query.all()
    booksStore = []
    for book in books:
        book_data =book.__dict__
        del book_data["_sa_instance_state"]
        booksStore.append(book_data)
    print(booksStore)
    return booksStore

category_serilizer= {
    "id": fields.Integer,
    "name":fields.String,
    "description":fields.String,
}

book_serilizer = {
    "id": fields.Integer,
    "name": fields.String,
    "image": fields.String,
    "price": fields.Integer,
    "NumberPage":fields.Integer,
    "category_id": fields.Integer,
    "category_name": fields.Nested(category_serilizer)
}

class BookList(Resource):
    @marshal_with(book_serilizer)
    def get(self):
        books = Book.query.all()
        return books , 200

    @marshal_with(book_serilizer)
    def post(self):
        print(request.data)
        book_data = books_parser.parse_args()
        print(book_data)
        book = Book.save_student(book_data)
        return book , 201




class BookResource(Resource):
    @marshal_with(book_serilizer)
    def get(self, book_id):
        book = Book.get_book_by_id(book_id)
        return book, 200

    @marshal_with(book_serilizer)
    def put(self, book_id):
        book = Book.get_book_by_id(book_id)
        if book:
            book_data = books_parser.parse_args()
            book.name = book_data["name"]
            book.image = book_data["image"]
            book.price =book_data["price"]
            book.NumberPage = book_data["NumberPage"]
            book.category_id =book_data["category_id"]
            db.session.add(book)
            db.session.commit()
            return book




    def delete(self, book_id):
        deleted = Book.delele_book(book_id)
        return deleted, 204
