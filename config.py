import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    generic config options
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("app-secret")
    POSTS_PER_PAGE = 10  # for pagination purposes


class DevConfig(Config):
    """
    config for development environment
    """
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"


class ProdConfig(Config):
    """
    config used in production environment
    """
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABSE_URL')


config_options = {
    'default': DevConfig,
    'development': DevConfig,
    'production': ProdConfig
}
