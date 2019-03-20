from sqlalchemy import Table, Column, Integer, String, ForeignKey

from connection import Base, engine


class Comment(Base):

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String(2000))
    post_id = Column(Integer, ForeignKey('posts.id'))

    def __repr__(self):
        return "<Comment (text='%s')>" % (self.text)
