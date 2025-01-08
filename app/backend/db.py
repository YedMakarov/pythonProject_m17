from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///taskmanager.db", echo=True)
# engine = create_engine("sqlite:///./taskmanager.db", echo=True)

# ----------------------
# import os
# engine = create_engine('sqlite:///' + os.path.join( os.path.abspath(os.path.dirname(__file__)), 'taskmanager.db'), echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
