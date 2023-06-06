from database_config import engine
from model.model import Base


Base.metadata.create_all(bind=engine)
