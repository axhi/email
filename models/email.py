import json
import re
import requests
from validate_email import validate_email

def missing_fields(value):
  return True if len(value) == 0 else False

def fix_body(body):
  return re.sub("<.*?>", " ", body).strip()

def process_email(email):
  response = {}
  try:
    data = json.loads(email)
    for field,value in data.items():
      if missing_fields(value):
        response = {'error':'All fields are required', 'status': 404}
        return response
  
    if not validate_email(data['to']) or not validate_email(data['from']):
        response = {'error':'Invalid email address', 'status': 404}
        return response

    data['body'] = fix_body(data['body'])
    response = data

  except TypeError:
    pass

  return response

def send_mail(mail):
  return requests.post(
      "https://api.mailgun.net/v2/sandboxe15c485216a2413fb340b1ac923a04c1.mailgun.org/messages",
      auth=("api", "key-dbb2bfcd4960249aa72fb68969ef4550"),
      data={"from": mail['from_name'] + "<" + mail['from'] + ">",
        "to": mail['to_name'] + "<"+ mail['to'] +">",
        "subject": mail['subject'],
        "text": mail['body']})
