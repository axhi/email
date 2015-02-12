from flask import request
from flask.ext.restful import Resource
from models.email import process_email, send_mail

class Email(Resource):
  def post(self):
    checked_mail = process_email(request.data)
    if 'error' in checked_mail:
      return 'Error: %s' %checked_mail['error']
    else:
      status = send_mail(checked_mail)
      return "Email sent and responded with: %s" %status
