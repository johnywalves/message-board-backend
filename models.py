from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

tags = Table('tag_post', Base.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id')),
    Column('post_id', Integer, ForeignKey('posts.id'))
)

class User(Base):

    __tablename__ = 'users'

    id          =   Column(Integer, primary_key=True)
    user        =   Column(String(50), nullable=False)
    password    =   Column(String(50), nullable=False)    

    def __repr__(self):
        return "<User (text='%d', likes='%d', created_at=%s)>" % (self.user)

class Post(Base):

    __tablename__ = 'posts'

    id          =   Column(Integer, primary_key=True)
    text        =   Column(String(2000), nullable=False)
    likes       =   Column(Integer, default=0)
    created_at  =   Column(DateTime, default=datetime.utcnow)
    tags        =   relationship('Tag', secondary=tags, backref=backref('posts', lazy='dynamic'))
    comments    =   relationship('Comment', cascade="all,delete", backref='post', lazy='dynamic')

    def __repr__(self):
        str_created_at = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return "<Post (text='%d', likes='%d', created_at=%s)>" % (self.text, self.likes, str_created_at)

class Tag(Base):

    __tablename__ = 'tags'

    id      =   Column(Integer, primary_key=True)
    name    =   Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<Tag (name='%s')>" % (self.name)

class Comment(Base):

    __tablename__ = 'comments'

    id          =   Column(Integer, primary_key=True)
    text        =   Column(String(2000))
    post_id    =   Column(Integer, ForeignKey('posts.id'))

    def __repr__(self):
        return "<Comment (text='%s')>" % (self.text)