import flask
from flask import Flask,jsonify,request,make_response
from flask_restful import Resource
app=flask.Flask(__name__)

products = [
    {"name": "caps",
    "price":  "23000",

},
 {"name": "jeans",
    "price"  :"1500",
 },
]

class Products(Resource):
    @app.route('/api/v1/product/',methods= ['GET'])
    def get(self, name):
        return make_response(jsonify({"message":"Successfully added to productss"}),201)
    
    