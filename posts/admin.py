from app import app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from posts.models import Post, Tag, db

admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))
