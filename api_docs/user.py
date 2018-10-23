from flask import Flask,jsonify,request
from flask_restful import Api,Resource,reqparse
from App import api

users = [
    {"name": "oscar",
    "email":  "nyebaoscar@gmail.com",
    "password": "supervisor",


},
 {"name": "dennis",
    "email"  :"denniskalema@gmail.com",
    "password" :"commonman",
 },
  {"name":"jonnas",
    "email": "jonnsa@gmail.com",
   git"password" :"attendant",
  },


]


class UserApi(Resource):
    
    @app.route('/name')
    def get(self, name):
    
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("password")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("email")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["email"] = args["email"]
                user["password"] = args["password"]
                return user, 200
        
        user = {
            "name": name,
            "email": args["email"],
            "password": args["password"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(user, "/user/<string:name>")

app.run(debug=True)