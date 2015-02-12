import json
from flask import Flask, request
from flask.ext.restful import Resource, Api
from models.email import process_email, send_mail

app = Flask(__name__)
api = Api(app)

class Email(Resource):
  def post(self):
    checked_mail = process_email(request.data)
    if 'error' in checked_mail:
      return 'Error: %s' %checked_mail['error']
    else:
      status = send_mail(checked_mail)
      return "Email sent and responded with: %s" %status

api.add_resource(Email, '/email')

if __name__ == '__main__':
  app.run(debug=True)
