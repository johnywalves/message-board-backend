from sqlalchemy import Table, Column, Integer, String, ForeignKey

from connection import Base, engine


class Tag(Base):

    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<Tag (name='%s')>" % (self.name)
