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

class Product(Resource):
    @app.route('/api/v1/product/',methods= ['GET'])
    def get(self, name):
        return make_response(jsonify({"message":"Successfully added to productss"}),201),
        
    @app.route('/api/v1/product/',methods= ['GET'])
    def get_products(self,public_id,product):
        product = product.query.filter_by(public_id=public_id).first()

        if not product:
            return jsonify({'message':'no product found'})

class sales(Resource):
    @app.route('/api/v1/product/',methods= ['GET'])
    def get_all_sales(self,sale,Sale):
        sale=Sale.get_sales()
        return jsonify(sales)
    def post(self,product_name,price,total_sale,quantity,sale_id):
        sale_id=len(sales)+1
        product_name=request.json.get('product_name')
        price =request.json.get('price')
        total_sale=request.json.get('total_sale')
        quantity=request.json.get('quantity')

        if product_name=="":
            return 404
            sale = Sale(sale_id,product_name,price,total_sale,quantity).create_sale()
            return make_response(jsonify({'sale':sale}),201)

    



        
