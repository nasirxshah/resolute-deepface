from flask_restful import Api
from app.home.resources import Index
api = Api()

api.add_resource(Index,"/")