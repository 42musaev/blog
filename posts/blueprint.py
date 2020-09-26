from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for

from .models import Post, Tag
from app import db
from .forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['GET', 'POST'])
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
            slug = post.slug
        except Exception as e:
            print(f'Some thing wrong: {e}')
        return redirect(url_for('posts.post_detail', slug=slug))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    query = request.args.get('query')
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if query:
        posts = Post.query.filter(
            Post.title.ilike(f"%{query}%") | Post.body.ilike(f"%{query}%")
        )
    else:
        posts = Post.query.order_by(Post.created.desc())
    pages = posts.paginate(page=page, per_page=6)
    return render_template(
        'posts/index.html',
        posts=posts,
        pages=pages,
        query=query,
    )


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post=post)


@posts.route('tag/<slug>')
def tag_posts(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_posts.html', tag=tag, posts=posts)
