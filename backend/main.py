from flask import Flask
from database_config import db_name
from routes import routes_bp
from models import db




def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_name
    app.register_blueprint(routes_bp)
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        port=8080,
        debug=True,
        host='localhost'
    )

