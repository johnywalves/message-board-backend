import os
from models import Base, User, Post, Tag, Comment

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.sql import desc

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'Adicionar-algum-texto-como-chave'
jwt = JWTManager(app)

engine = create_engine('sqlite:///mydb.db', poolclass=SingletonThreadPool)

def postJSON(post):
    if post is not None:
        tags = []
        for tag in post.tags:
            tags.append({'name':tag.name})

        comments = []
        for comment in post.comments:
            comments.append({'id':comment.id, 'text':comment.text})

        return {'id':post.id, 'text':post.text, 'likes':post.likes, 'created_at':post.created_at.strftime('%Y-%m-%d %H:%M:%S'), 'tags':tags, 'comments':comments}
    else:
        return {}

class loginAPI(Resource):
    def post(self):
        session = sessionmaker(bind=engine)()
        data = request.json
        user = session.query(User).filter(User.user == data['user']).one_or_none()
        if user is not None:
            if user.password == data['pass']:
                current_user = get_jwt_identity()
                access_token = create_access_token(identity = current_user)
                return {'token': access_token}
            else:
                return {}
        else:
            return {}

class postsAPI(Resource):
    def get(self):
        session = sessionmaker(bind=engine)()
        posts = []
        for post in session.query(Post).order_by(desc(Post.created_at)):
            posts.append(postJSON(post))
        return posts

    @jwt_required
    def post(self):
        session = sessionmaker(bind=engine)()
        data = request.json

        tags = []
        for etiqueta in data['tags']:
            tag = session.query(Tag).filter(Tag.name == etiqueta['name']).first()
            if tag is None:
                tag = Tag(name=etiqueta['name'])
                session.add(tag)
            tags.append(tag)

        comments = []
        for comentario in data['comments']:
            comment = Comment(text=comentario['text'])
            session.add(comment)
            comments.append(comment)

        post = Post(text=data['text'], tags=tags, comments=comments)
        session.add(post)
        session.commit()

        return postJSON(post)

class postsTagAPI(Resource):
    def get(self, tag):
        session = sessionmaker(bind=engine)()
        posts = []
        for post in session.query(Post).join(Tag, Post.tags).filter(Tag.name == tag):
            posts.append(postJSON(post))
        return posts

class postsIdAPI(Resource):
    @jwt_required
    def get(self, id):
        session = sessionmaker(bind=engine)()
        post = session.query(Post).filter(Post.id == id).one_or_none()
        return postJSON(post)

    @jwt_required
    def put(self, id):
        session = sessionmaker(bind=engine)()
        data = request.json
        post = session.query(Post.id, Post.text).filter(Post.id == id).one_or_none()

        if post is not None:
            post.text = data['text']
            post.likes = data['likes']
            session.commit()

            return postJSON(post)
        else:
            return {}

    @jwt_required
    def delete(self, id):
        session = sessionmaker(bind=engine)()
        post = session.query(Post).filter(Post.id == id).first()
        session.delete(post)
        session.commit()
        return {'success':'true'}

class likeAPI(Resource):
    @jwt_required
    def post(self, id):
        session = sessionmaker(bind=engine)()
        post = session.query(Post).filter(Post.id == id).first()
        post.likes = post.likes + 1
        session.commit()
        return {'success':'true'}

    @jwt_required
    def delete(self, id):
        session = sessionmaker(bind=engine)()
        post = session.query(Post).filter(Post.id == id).first()
        post.likes = post.likes - 1
        session.commit()
        return {'success':'true'}

class commentAPI(Resource):
    @jwt_required
    def post(self, id):
        session = sessionmaker(bind=engine)()
        data = request.json

        comment = Comment(text=data['text'])

        post = session.query(Post).filter(Post.id == id).first()
        post.comments.append(comment)

        session.add(comment)
        session.commit()

        return postJSON(post)

api.add_resource(loginAPI, '/v1.0/login')
api.add_resource(postsAPI, '/v1.0/posts')
api.add_resource(postsIdAPI, '/v1.0/posts/<int:id>')
api.add_resource(postsTagAPI, '/v1.0/posts/<string:tag>')
api.add_resource(likeAPI, '/v1.0/posts/<int:id>/like')
api.add_resource(commentAPI, '/v1.0/posts/<int:id>/comments')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
