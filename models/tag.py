from sqlalchemy import Table, Column, Integer, String, ForeignKey

from connection import Base, engine
from functions import toJSON, fromJSON


class Tag(Base):

    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<Tag (name='%s')>" % (self.name)

    def toJson(self): return toJSON(self)

    def fromJson(self, data): return fromJSON(self, data)
