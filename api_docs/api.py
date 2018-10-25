
from flask import Flask,jsonify,request,make_response
from flask_restful import Resource,Api
import json

app= Flask(__name__)

products = []

@app.route('/')
def index():
    return "welcome"

@app.route('/api/v1/create/',methos='POST')
def create_product():

    product_dict={ 
        "product_id": request.json["product_id"],
        "product name": request.json["product_name"],
        "product price": request.json["product_price"],
        "product quantity": request.json["product_quantity"]
    }
    products.append(product_dict)
    return jsonify (products)


@app.route('/api/v1/product/',methods= ['GET'])
def get():
    return jsonify({"message":"Successfully added to productss"}),201

        
@app.route('/api/v1/product/<name>',methods= ['GET'])
def get_products(name):
    for product in products:
        for key in product: 
            if product[key] == name:
                return jsonify(product)

            if not product[key]:
                return jsonify({'message':'no product found'})


@app.route('/api/v1/sales/',methods= ['GET'])
def get_all_sales():
    sale=Sale.get_sales()
    return jsonify(sales)

def post():
    sale_id=len(sales)+1
    product_name=request.json.get('product_name')
    price =request.json.get('price')
    total_sale=request.json.get('total_sale')
    quantity=request.json.get('quantity')

if product_name== " ":
    return jsonify ({'message':"not available"}),404
   # sale = Sale(sale_id,product_name,price,total_sale,quantity).create_sale()
    # return (jsonify({'sale':sale}),201)


@app.route('/api/v1/slaes/id/',methods=['GET'])
def get_sales_by_id(sales,sale_id):
    sal = [sale for sale in sales if sale['sale_id'] == sale_id] or None
    if sal:
        return make_response(jsonify({'sale':sal[0]}),200)
    else:
        return jsonify({'message': "specific sale not found"})
            

    return 404

if __name__=="__main__":
    app.run(debug=True)


        
