from database_config import engine
from model.model import Base

try:
    Base.metadata.create_all(engine)
    print("Tables created successfully.")
except Exception as e:
    print("Error occurred:", e)

