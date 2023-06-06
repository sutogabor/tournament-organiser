from flask import Flask
from database_config import db_name
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = db_name

db = SQLAlchemy()

db.init_app(app)


if __name__ == "__main__":
    app.run(
        debug=True,
        host='localhost',
        port=8080
    )

