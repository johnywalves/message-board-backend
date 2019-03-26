from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from connection import Base, engine
from functions import toJSON, fromJSON

tags = Table('tag_post', Base.metadata,
             Column('tag_id', Integer, ForeignKey('tags.id')),
             Column('post_id', Integer, ForeignKey('posts.id'))
             )


class Post(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    text = Column(String(2000), nullable=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    tags = relationship('Tag', secondary=tags,
                        backref=backref('posts', lazy='dynamic'))
    comments = relationship('Comment', cascade="all,delete",
                            backref='post', lazy='dynamic')

    def __repr__(self):
        str_created_at = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return "<Post (text='%d', likes='%d', created_at=%s)>" % (self.text, self.likes, str_created_at)

    def toJson(self): return toJSON(self)

    def fromJson(self, data): return fromJSON(self, data)
