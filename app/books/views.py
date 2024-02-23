from flask import render_template, request, redirect, url_for, flash
from models import  Book, db
from flask import request
from books import book_blueprint
from datetime import datetime
from werkzeug.utils import secure_filename
from .forms import BookForm

def get_index():
    return "<h1> Index </h1> "


@book_blueprint.route('', endpoint='index')
def books_index():
    book = Book.get_all_objects()
    return  render_template("book/index.html", book=book)


@book_blueprint.route("/<int:id>", endpoint="show")
def books_show(id):
    book = Book.get_book_by_id(id)
    if book:
        return render_template("book/show.html", book=book)
    else:
        flash("Book not found", "error")
        return redirect(url_for("books.index"))

@book_blueprint.route("/create", methods=['GET', 'POST'],
                         endpoint='create')
def create_book():
    if request.method == 'POST':
        print(f"request received > {request.form}")
        book = Book.save_book(request.form)
        return redirect(book.show_url)

    return render_template("book/create.html")



@book_blueprint.route("/delete/<int:id>", methods=['GET', 'POST'], endpoint='delete')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.index'))




@book_blueprint.route("/update/<int:id>", methods=['GET', 'POST'], endpoint='update')
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.name = request.form['name']
        book.price = request.form['price']
        book.image = request.form['image']
        book.NumberPage=request.form['NumberPage']
        book.updated_at = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('books.show', id=book.id))
    return render_template("book/update.html", book=book)


@book_blueprint.route("/createform", methods=['GET', 'POST'], endpoint='createform')
def create_book_viaform():
    form = BookForm()
    if form.validate_on_submit():
        book_data = {
            'name': form.name.data,
            'price': form.price.data,
            'NumberPage': form.NumberPage.data,
            'image': form.image.data,
            'category_id': form.category_id.data.id  
        }
        book = Book.save_book(book_data)
        return redirect(book.show_url)

    return render_template("book/createform.html", form=form)




@book_blueprint.route('/updateform/<int:id>', methods=['GET', 'POST'], endpoint='updateform')
def update_book(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        category_id = form.category_id.data.id
        
        book.name = form.name.data
        book.price = form.price.data
        book.NumberPage = form.NumberPage.data
        book.image = form.image.data
        book.category_id = category_id 
        
        db.session.commit()
        flash('Book updated successfully', 'success')
        return redirect(url_for('books.show', id=book.id))
    return render_template('book/updateform.html', form=form, book=book)

