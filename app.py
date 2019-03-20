import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import desc

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from passlib.hash import pbkdf2_sha256 as sha256

from controllers import loginAPI, postsAPI, postsIdAPI, postsTagAPI, likeAPI, commentAPI

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'Adicionar-algum-texto-como-chave'
jwt = JWTManager(app)

api.add_resource(loginAPI, '/v1.0/login')
api.add_resource(postsAPI, '/v1.0/posts')
api.add_resource(postsIdAPI, '/v1.0/posts/<int:id>')
api.add_resource(postsTagAPI, '/v1.0/posts/<string:tag>')
api.add_resource(likeAPI, '/v1.0/posts/<int:id>/like')
api.add_resource(commentAPI, '/v1.0/posts/<int:id>/comments')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
