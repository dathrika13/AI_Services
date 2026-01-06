from src import config

from sqlalchemy import create_engine, Column, String, Integer, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config.get_connection_string())

Base = declarative_base()

class Attachment(Base):
    __tablename__ = 'attachments'
    # TODO: Add the columns here

class Job(Base):
    __tablename__ = 'jobs'
    # TODO: Add the columns here

class Collection(Base):
    __tablename__ = 'collections'
    # TODO: Add the columns here


# # Create the table
# Base.metadata.create_all(engine)
