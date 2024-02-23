from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime

db = SQLAlchemy()
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description  = db.Column(db.String)
    books = db.relationship('Book', backref='category_name', lazy=True)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()

    @classmethod
    def save_category(cls, category_data):
        category = cls(**category_data)
        db.session.add(category)
        db.session.commit()
        return category
    
    def save(self):
        db.session.commit()
     
     
    def delete(self):
        db.session.delete(self)
        db.session.commit()
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    name = db.Column(db.String)
    NumberPage = db.Column(db.Integer)
    image = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  
    category_id =db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)


    def __str__(self):
        return self.name


    @property
    def image_url(self):
        return url_for('static', filename=f'students/images/{self.image}')

    @property
    def show_url(self):
        return url_for("books.show", id = self.id)

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()

    @classmethod
    def get_book_by_id(cls, id):
        return  cls.query.get_or_404(id)

    @classmethod
    def save_book(cls, request_data): 
        book = cls(**request_data)
        db.session.add(book)
        db.session.commit()
        return book

    
