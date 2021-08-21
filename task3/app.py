from flask import Flask, request
from flask_restful import Api, Resource

from find_sum import calculate_sum

app = Flask(__name__)
api = Api(app)

class SumAPI(Resource):
    """
    API to accept input as json in put request and returns the calculated sum
    """
    def put(self):
        args = request.get_json(force=True)
        calculated_sum = calculate_sum(args)
        return {"status": calculated_sum[0], "result": calculated_sum[1]}

api.add_resource(SumAPI, '/sum')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)