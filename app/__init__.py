from flask import  Flask
from config import config_options as AppConfig
from models import  db

from flask_migrate import Migrate
from flask_restful import  Api




def create_app(config_name="prd"):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    print(current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config)


    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)


    from books import book_blueprint
    app.register_blueprint(book_blueprint)
    from categories import  category_blueprint
    app.register_blueprint(category_blueprint)
    
    


    api = Api(app)
    from books.api_views import  BookList, BookResource
    api.add_resource(BookList,'/api/books' )
    api.add_resource(BookResource, '/api/books/<int:book_id>')
    
    
    return app