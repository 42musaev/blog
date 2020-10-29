from users.models import User, Role
from app import app
from app import db

from posts.blueprint import posts
from users.blueprint import users

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security

import view
import admin


app.register_blueprint(posts, url_prefix='/blog')


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


if __name__ == '__main__':
    app.run()
