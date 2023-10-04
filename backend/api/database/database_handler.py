from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
from api.database.database_config import engine, base

db = SQLAlchemy()


def create_tables_if_not_exist():
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    table_names_to_create = [table_name for table_name in base.metadata.tables.keys() if table_name not in existing_tables]

    if table_names_to_create:
        base.metadata.create_all(bind=engine, )


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        