import os

from flask import current_app, request
from flask_restful import Resource

from app.df import services
from app.df.models import User
from app.extensions import db


class Register(Resource):
    def post(self):
        body = request.get_json()
        if (
            body.get("username") is None
            or body.get("email") is None
            or body.get("img") is None
        ):
            return {
                "username": "field required",
                "email": "field required",
                "img": "field required",
            }, 400

        user = db.session.query(User).filter(User.username == body['username']).scalar()
        if user:
            return {"status":"error","message":"username already exists"},400

        database = os.path.join(
            current_app.instance_path, current_app.config["DEEPFACE_DATABASE"]
        )

        result = services.recognise(img=body['img'],db_path=current_app.instance_path)
        if result['status'] == "error":
            result2 = services.register(body["username"], body["img"], database)
            if result2["status"] == "success":
                user = User(username=body["username"], email=body["email"])
                db.session.add(user)
                db.session.commit()
                return {"username": user.username, "email": user.email}, 201
            else:
                return result2, 400
        else:
            return {"status":"error","message":"user already exists"}, 400

class Recognise(Resource):
    def post(self):
        body = request.get_json()
        if body.get("img") is None:
            return {"img": "field required"}, 400

        result = services.recognise(body["img"], db_path=current_app.instance_path)

        if result['status'] == "error":
            return result,400
        
        identity = result['identity']
        user = db.session.query(User).filter(User.username == identity).scalar()

        return {"username": user.username, "email": user.email}
