from flask import jsonify
from flask_restful import Api, Resource
import config

api = Api(prefix=config.API_PREFIX)


class ProductsAPI(Resource):
    def get(self):
        return jsonify({ "response": "Hello" })

# task status endpoint
api.add_resource(ProductsAPI, '/products')
