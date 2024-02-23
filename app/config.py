import os
class Config:
    SECRET_KEY = os.urandom(32)
    @staticmethod
    def init_app():
        pass



class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///project.db'



class ProductionConfig(Config):
    DEBUG=False
    """postgresql://username:password@localhost:portnumber/database_name """
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:khaled00@localhost:5432/books'



config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}