import json
from flask import Flask
from resources.email import Email
from flask.ext.restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Email, '/email')

if __name__ == '__main__':
  app.run(debug=True)
