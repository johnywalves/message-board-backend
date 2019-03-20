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
