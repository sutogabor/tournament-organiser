from flask import Flask
from api.database.database_config import url_object
from api.routes import routes_bp
from api.database.database_handler import init_db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = url_object
    app.register_blueprint(routes_bp)
    init_db(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        port=8080,
        debug=True,
        host='localhost'
    )
