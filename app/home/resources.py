from flask_restful import Resource


class Index(Resource):
    def get(self):
        return {"status": "ok", "details": "server is up and running"}
