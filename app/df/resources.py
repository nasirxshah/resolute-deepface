import os

from flask import current_app, request
from flask_restful import Resource

from app.df import controller
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
            }

        db_path = os.path.join(
            current_app.instance_path, current_app.config["DEEPFACE_DATABASE"]
        )
        controller.register(body["username"], body["img"], db_path)

        user = User(username=body["username"], email=body["email"])
        db.session.add(user)
        db.session.commit()

        return {"username": user.username, "email": user.email}


class Recognise(Resource):
    def post(self):
        body = request.get_json()
        if body.get("img") is None:
            return {"img": "field required"}

        identity = controller.recognise(body["img"], db_path=current_app.instance_path)

        if identity:
            user = db.session.query(User).filter(User.username == identity).scalar()

            return {"username": user.username, "email": user.email}
        return {"status": "error", "details": "user details not found"}
