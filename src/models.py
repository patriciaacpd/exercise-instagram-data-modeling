import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User (Base):
    __tablename__= "user"
    id = Column(Integer, primary_key = True)
    email = Column(String(30), nullable = False, unique = True)
    username = Column(String(30), nullable = False , unique = True)
    password = Column(String(30), nullable = False)
    firstname = Column(String(30), nullable = False)
    lastname = Column(String(30), nullable = False)   
    post = relationship("post") 
    comment = relationship ("comment")  
    followers = relationship ("follower")

class Follower (Base):
    __tablename__= "follower"
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, nullable = False)
    user_to_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    user = relationship(User)


class Post (Base):
    __tablename__= "post"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    url = Column(String(30), nullable = False)
    user = relationship("user")   
    comment = relationship("comment")

class Like (Base):
    __tablename__= "like"
    id = Column(Integer, primary_key = True)
    author_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    post = relationship("post")
    user = relationship("user")  


class Comment (Base):
    __tablename__= "comment"
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(30), nullable = False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    user = relationship("user")  
    post = relationship ("post")
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
