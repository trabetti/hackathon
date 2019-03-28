from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

answers = [
    {
        "name": "Ronny",
        "answer":[]
        # "age": 42,
        # "occupation": "Network Engineer",
        # "rating":4.3,
        # "subjects":"build-wix-site,google-cloud"
    },
    {
        "name": "Miri",
        "age": 32,
        "occupation": "solution architect",
        "rating":5.0,
        "subjects":"google-cloud,write-cv"
    },
]

user1 = {
        "name": "roni",
        "age": 42,
        "occupation": "Network Engineer",
        "rating":4.3,
        "subjects":"build-wix-site,google-cloud"
    }

user2 = {
        "name": "Miri",
        "age": 32,
        "occupation": "solution architect",
        "rating":5.0,
        "subjects":"google-cloud,write-cv"
    }

user3 = {
        "name": "Noga",
        "age": 22,
        "occupation": "Web Developer",
        "rating":3.4,
        "subjects":"mobile-ux,write-cv"
    }

user4 =  {
        "name": "Alex",
        "age": 22,
        "occupation": "account-manager",
        "rating":3.4,
        "subjects":"ad-tech,write-cv"
    }

class User(Resource):
    def get(self, name):
        for user in users:
            if (name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
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
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


class Recommendation(Resource):
    def get(self, name):
        if recommendations[name]:
            return recommendations[name], 200
        return "User not found", 404

class Question(Resource):
    def get(self, name):
        if answers[name]:
            return answers[name], 200
        return "User not found", 404

    # def post(self, name):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("age")
    #     parser.add_argument("occupation")
    #     args = parser.parse_args()
    #
    #     for user in users:
    #         if (name == user["name"]):
    #             return "User with name {} already exists".format(name), 400
    #
    #     user = {
    #         "name": name,
    #         "age": args["age"],
    #         "occupation": args["occupation"]
    #     }
    #     users.append(user)
    #     return user, 201

    # def put(self, name):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("age")
    #     parser.add_argument("occupation")
    #     args = parser.parse_args()
    #
    #     for user in users:
    #         if (name == user["name"]):
    #             user["age"] = args["age"]
    #             user["occupation"] = args["occupation"]
    #             return user, 200
    #
    #     user = {
    #         "name": name,
    #         "age": args["age"],
    #         "occupation": args["occupation"]
    #     }
    #     users.append(user)
    #     return user, 201
    #
    # def delete(self, name):
    #     global users
    #     users = [user for user in users if user["name"] != name]
    #     return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")
api.add_resource(Question, "/question/<string:name>")

if __name__ == '__main__':
    users = []
    users.append(user1)
    users.append(user2)
    users.append(user3)
    users.append(user4)
    answers = {}
    answers["roni"] = [user1,user2]
    recommendations = {}
    recommendations["roni"] = [user3,user4]
    port = int(os.getenv('PORT', 5002))
    app.run(host='0.0.0.0', port=port)
