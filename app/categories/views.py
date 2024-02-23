from flask import render_template, redirect, url_for, flash
from .forms import CategoryForm
from models import Category, db
from . import category_blueprint
from sqlalchemy.exc import IntegrityError




@category_blueprint.route('/home', methods=['GET'], endpoint='home')
def category_home():
    return "<h1>Category Hub</h1>"



@category_blueprint.route('/', methods=['GET'], endpoint='index')
def category_index():
    categories = Category.get_all_categories()
    return render_template("categories/index.html", categories=categories)



@category_blueprint.route('/createCategory', methods=['GET', 'POST'], endpoint='createCategory')
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category_data = {
            'name': form.name.data,
            'description': form.description.data
        }
        Category.save_category(category_data)
        flash('Category is created Successfully', 'success')
        return redirect(url_for('category.index'))
    return render_template('categories/createCategory.html', form=form)




@category_blueprint.route('/updateCategory/<int:category_id>', methods=['GET', 'POST'], endpoint='updateCategory')
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        new_name = form.name.data
        if new_name != category.name:
            existing_category = Category.query.filter_by(name=new_name).first()
            if existing_category:
                flash('This name is already exists', 'error')
                return redirect(url_for('category.updateCategory', category_id=category_id))

        try:
            form.populate_obj(category)
            category.save()  
            flash('Category updated Successfully', 'success')
            return redirect(url_for('category.index'))
        except IntegrityError as e:
            flash('Error on update Category', 'error')
            return redirect(url_for('category.updateCategory', category_id=category_id))

    return render_template('categories/updateCategory.html', form=form, category=category)





@category_blueprint.route('/deleteCategory/<int:category_id>', methods=['POST'], endpoint='deleteCategory')
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('category.index'))
