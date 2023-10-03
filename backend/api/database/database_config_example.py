from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, Session

url_object = URL.create(
    "dialect+driver",
    username="my_username",
    password="my_password",  # plain (unescaped) text
    host="localhost",
    database="my_dbname",
)

engine = create_engine(url_object)
base = declarative_base()
