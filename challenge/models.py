from pyramid.security import Allow, Everyone
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Session(Base):
    __tablename__ = 'sessions_table'
    uid = Column(Integer, primary_key=True)
    info = Column(Text)

class Access(Base):
    __tablename__ = 'accesses_table'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions_table.uid'))
    page = Column(Text)
    datetime = Column(Text)

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass