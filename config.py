import os

class Config:
    '''
    General configuration parent class
    '''
    
    QUOTE_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adriantuimur://qweasdzxc1234567890@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class TestConfig(Config):
    pass



class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adriantuimur://qweasdzxc1234567890@localhost/blog'
    
    DEBUG = True
    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}