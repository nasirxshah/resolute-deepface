from flask import Flask

from app.df import df_blueprint
from app.extensions import db
from app.home import home_blueprint


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(df_blueprint)
    app.register_blueprint(home_blueprint)

    return app
