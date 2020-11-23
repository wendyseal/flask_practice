from flask import Flask, render_template
from flask_restful import Api 

from resources.user import User, Users, PrintHelloWorld


app = Flask(__name__)
api = Api(app)
# 把User綁定到url/user/
api.add_resource(User, "/user/<string:name>")
api.add_resource(Users, "/users/")
api.add_resource(PrintHelloWorld, "/printhelloworld/")

@app.route("/")
def hello():
    return render_template('hello.html')


if __name__ == "__main__":
    from common.ma import ma
    ma.init_app(app)
    app.run(
        host="0.0.0.0",
        debug=True,
        # use_reloader=True,
        # threaded=True
        )



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return "post mode: <create>201 (Created), 'Location' header with link to /customers/ containing new ID"
#     else:
#         return "get mode: <read>200 (OK), list of customers. Use pagination, sorting and filtering to navigate big lists."

# @app.route('/login', methods=['PUT', 'PATCH'])
# def login():
#     if request.method == 'POST':
#         return "PUT mode"
#     else:
#         return "PATCH mode"