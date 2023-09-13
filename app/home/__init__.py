from flask import Blueprint

from app.home.routes import api

home_blueprint = Blueprint("home", __name__)
api.init_app(home_blueprint)
