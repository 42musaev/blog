from app import app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from posts.models import Post, Tag, db
from users.models import User, Role
from flask_security import current_user
from flask_admin import AdminIndexView

from flask import redirect, url_for, request


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(
            BaseModelView,
            self).on_model_change(
            form,
            model,
            is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView):
    pass


class TagAdminView(AdminMixin, BaseModelView):
    pass


admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))
