from flask import Blueprint
from app.df.routes import api

df_blueprint = Blueprint("df", __name__)
api.init_app(df_blueprint)
