from database_config import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

try:
    Base.metadata.create_all(engine)
    print("Tables created successfully.")
except Exception as e:
    print("Error occurred:", e)

