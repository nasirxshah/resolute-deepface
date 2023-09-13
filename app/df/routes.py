from flask_restful import Api

from app.df.resources import Recognise, Register

api = Api()
api.add_resource(Register, "/register")
api.add_resource(Recognise, "/recognise")
