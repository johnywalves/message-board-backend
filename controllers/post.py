import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import desc

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from passlib.hash import pbkdf2_sha256 as sha256

from connection import Base, engine
from functions import postJSON
from models import User, Post, Tag, Comment


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
            tag = session.query(Tag).filter(
                Tag.name == etiqueta['name']).first()
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
        post = session.query(Post.id, Post.text).filter(
            Post.id == id).one_or_none()

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
        return {'success': 'true'}


class likeAPI(Resource):
    @jwt_required
    def post(self, id):
        session = sessionmaker(bind=engine)()
        post = session.query(Post).filter(Post.id == id).first()
        post.likes = post.likes + 1
        session.commit()
        return {'success': 'true'}

    @jwt_required
    def delete(self, id):
        session = sessionmaker(bind=engine)()
        post = session.query(Post).filter(Post.id == id).first()
        post.likes = post.likes - 1
        session.commit()
        return {'success': 'true'}
