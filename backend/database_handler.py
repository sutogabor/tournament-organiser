from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("localhost://5000/my_db")
session = sessionmaker(engine)
base = declarative_base()
