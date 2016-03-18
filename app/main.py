from flask import Flask, request
from flask_restful import Resource, Api
from passwd_gen import Password

app = Flask(__name__)
api = Api(app)

class PasswordResource(Resource):

    def get(self):

        password_length = int(request.args.get('length',8))
        contains_letters = bool(request.args.get('contains_letters', True))
        mixed_case = bool(request.args.get('mixed_case', True))
        numbers = bool(request.args.get('numbers', True))
        punctuation = bool(request.args.get('punctuation',False))

        p = Password(length=password_length, letters=contains_letters, mixedcase=mixed_case, numbers=numbers, punctuation=punctuation)

        password = p.create_password(repeat=(password_length>20))
        remember = p.remember_password(password)



        return {'password': password,'remember':remember}

api.add_resource(PasswordResource, '/')

if __name__ == '__main__':
    app.run(debug=True)