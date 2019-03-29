from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import os
import json
# get this object
from flask import Response

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
        "rating":150,
        "subjects":"google-cloud,write-cv"
    },
]

user1 = {
        "name": "Roni",
        "age": 42,
        "occupation": "Network Engineer",
        "rating":403,
        "subjects":"build-wix-site,google-cloud",
        "phone":"0548887371",
    "reviews": "Roni has a lot of knowledge on networks and she is happy to share it.",
    "image":"mentor13.png"
    }

user2 = {
        "name": "Miri",
        "age": 32,
        "occupation": "solution architect",
        "rating":50,
        "subjects":"google-cloud, write-cv",
        "phone":"0542545499",
    "reviews": "Miri helped me write an awesome cv that helped me find a new job.",
    "image":"mentor10.png"
    }

user3 = {
    "name": "Tal Zavitan",
    "occupation": "customer success",
    "rating": 776,
    "subjects": "promotion, surfing",
    "phone": "0549107233",
    "reviews": "very helpful conversation, thanks!",
    "image": "mentor2.png"
}

user4 =  {
        "name": "Ziv Ambar",
        "occupation": "python developer",
        "rating":340,
        "subjects":"python, write-cv",
        "phone":"0548887371",
    "reviews": "Ziv helped me write an awesome cv that helped me find a new job.",
    "image":"mentor11.png"
    }

user5 =  {
        "name": "Noga",
        "age": 22,
        "occupation": "Web Developer",
        "rating":110,
        "subjects":"mobile-ux, write-cv, html",
        "phone":"0525640160",
    "reviews": "Noga has a lot of knowledge in web development and she is happy to share it.",
    "image":"mentor9.png"
    }

user6 =  {
        "name": "Gonen Shelef",
        "occupation": "biz dev",
        "rating":304,
        "subjects":"ad-tech, bitcoin, hiking",
        "phone":"0525640160",
    "reviews": "very helpful conversation, thanks!",
    "image":"mentor14.png"
    }

user7 =  {
        "name": "Ran Adam",
        "occupation": "IT",
        "rating":99,
        "subjects":"cloud, devops",
        "phone":"0549107233",
    "reviews": "very helpful conversation, thanks!",
    "image":"mentor7.png"
    }

class User(Resource):
    def get(self, index):
        # if index == "all":
        #     return Response(json.dumps([{"a":"1"},{"b":"2"}]),  mimetype='application/json')
        user=None
        try:
            iid = int(index)
            user = users[iid]
        except ValueError as e:
            for u in users:
               if (index == u["name"]):
                   user = u
        if user:
            return Response(json.dumps(user), mimetype='application/json')
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
                ret = user
                return Response(json.dumps(ret), mimetype='application/json'), 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        ret = user
        return Response(json.dumps(ret), mimetype='application/json'), 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


class Recommendation(Resource):
    def get(self, name):
        if recommendations[name]:
            ret = recommendations[name]
            return Response(json.dumps(ret), mimetype='application/json'), 200
        return "User not found", 404

class Question(Resource):
    def get(self, name):
        if answers[name]:
            ret = answers[name]
            return Response(json.dumps(ret), mimetype='application/json'), 200
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


api.add_resource(User, "/user/<string:index>")
api.add_resource(Question, "/question/<string:name>")
api.add_resource(Recommendation, "/recommendation/<string:name>")

if __name__ == '__main__':
    users = []
    users.append(user1)
    users.append(user2)
    users.append(user3)
    users.append(user4)
    users.append(user5)
    users.append(user6)
    users.append(user7)
    answers = {}
    answers["roni"] = [user1,user2]
    recommendations = {}
    recommendations["roni"] = [user3,user4]
    port = int(os.getenv('PORT', 5002))
    app.run(host='0.0.0.0', port=port)
