class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://flask_user:1234@localhost/flask_db"
    SECRET_KEY = "p7raa=65lu)(5+2j0&qor&5+-h1zp7fkx^+=qg%@8l%ib2ym)w"

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
