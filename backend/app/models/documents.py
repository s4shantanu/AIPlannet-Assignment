from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password_hash = Column(String(128))

class Document(Base):
    __tablename__ = 'documents'
    document_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    upload_date = Column(DateTime)
    s3_url = Column(String(500))
    metadata = Column(Text)

class UserDocument(Base):
    __tablename__ = 'user_documents'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    document_id = Column(Integer, ForeignKey('documents.document_id'))
