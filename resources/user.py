from flask_restful import Resource, reqparse
from flask import request

from models.schema.user_schema import UserSchema

# users = [{
#     'name' : 'Wendy',
#     # 'name' : 'Karen',
#     # 'name' : 'Leo'
# }]
users = []
user_schema = UserSchema()


class Users (Resource):
#定義欲接受請求的參數內容
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Email is required')
    parser.add_argument('password', required=True, help='Password is required')

    # # Look only in the POST body
    # parser.add_argument('name', type=int, location='form')

    # # Look only in the querystring
    # parser.add_argument('name', type=int, location='args')

    # # Look only in the json
    # parser.add_argument('name', type=int, location='json')

    # # Look only in the multi location
    # parser.add_argument('name', type=int, location=['form', 'json'])

    def get(self):
        return {
            'message' : 'Hi',
            'users': users
        }
    
class User (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Email is required')
    parser.add_argument('password', required=True, help='Password is required')
    
    def get(self, name):
        find = [item for item in users if item['name'] == name]
        if len(find) == 0:
            return {
                'message' : 'username not exist!'
            },403
        user = find[0]
        if not user:
            return {
                'message' : 'username not exist!'
            },403
        return {
            'message' : 'Hi',
            'user': user
        }

    def post(self, name):
        # arg = self.parser.parse_args()
        # user = {
        #     'name': name,
        #     'email': arg['email'],
        #     'password': arg['password']
        # }
        result = user_schema.load(request.json)

        if len(result.errors) > 0:
            return result.errors, 433

        user = {
            'name': name,
            'email': result.data['email'],
            'password': result.data['password']
        }
        global users
        users.append(user)
        return {
            'message': 'Insert user success',
            'user': user
        }

    # 完整更新資料0
    def put(self, name):
        # arg = self.parser.parse_args()
        # find = [item for item in users if item['name'] == name]
        # if len(find) == 0:
        #     return {
        #         'message': 'username not exist!'
        #     }, 403
        # user = find[0]
        # user['email'] = arg['email']
        # user['password'] = arg['password']
        result = user_schema.load(request.json)

        if len(result.errors) > 0:
            return result.errors, 433

        find = [item for item in users if item['name'] == name]
        if len(find) == 0:
            return {
                'message': 'username not exist!'
            }, 403
        user = find[0]
        user['email'] = result.data['email']
        user['password'] = result.data['password']

        return {
            'message': 'Update user success',
            'user': user
        }


    def delete(self, name):
        global users 
        users = [item for item in users if item['name'] != name]
        return {
            'message' : 'Delete done!'
        }
    

# json_data = request.json # json_data = request.form
# result = user_schema.load(json_data)

# if len(result.errors) > 0:
#     return result.errors, 433

# user = {
#     'name': name,
#     'email': result.data['email'],
#     'password': result.data['password']
# }

# 新增一個resource，而restful就是以資源為基礎，每一個項目都可以是一個資源
# 建立一個新的項目繼承Resource
class PrintHelloWorld(Resource):
    #客戶端的請求所需提交的method-當伺服器端收到這method的請求, 返還一個JSON的訊息格式以及status
    def get(self):
        return{
            'message':'Hello World!'
        }, 200
