import os

DEBUG = os.getenv('DEBUG', True)
SECRET_KEY = os.getenv('SECRET_KEY', 'this-is-a-super-secret-key')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite')
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = os.getenv('MAIL_PORT', 465)
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', True)
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'myemailhere@gmail.com')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'something here')
