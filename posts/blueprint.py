from flask import Blueprint
from flask import render_template
from flask import request

from .models import Post, Tag
# from sqlalchemy import func

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    query = request.args.get('query')

    if query:
        posts = Post.query.filter(
            Post.title.ilike(f"%{query}%") | Post.body.ilike(f"%{query}%")
        ).all()
    else:
        posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post=post)


@posts.route('tag/<slug>')
def tag_posts(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_posts.html', tag=tag, posts=posts)
