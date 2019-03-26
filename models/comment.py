from sqlalchemy import Table, Column, Integer, String, ForeignKey

from connection import Base, engine
from functions import toJSON, fromJSON


class Comment(Base):

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String(2000))
    post_id = Column(Integer, ForeignKey('posts.id'))

    def __repr__(self):
        return "<Comment (text='%s')>" % (self.text)

    def toJson(self): return toJSON(self)

    def fromJson(self, data): return fromJSON(self, data)
