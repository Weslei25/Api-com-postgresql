from flask_restful import Resource

class Conctacs(Resource):
    def get(self):
        return {"message": " Fala Thiago Sua Api esta aqui"}

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass