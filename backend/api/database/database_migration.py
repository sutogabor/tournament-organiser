from api.database.database_config import engine
from api.models.models import Base

Base.metadata.create_all(bind=engine)
