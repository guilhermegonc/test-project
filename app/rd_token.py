import os
import requests
import json


def get_valid_token(path):
  token = load_last_token(path)
  token = token if is_valid(token) else refresh(token)

  with open(path, 'w') as file:
    json.dump(token, file)

  return {'Authorization': 'Bearer ' + token['access_token']}


def load_last_token(path):
  with open(path, 'r') as file:
    return json.load(file)


def is_valid(token):
  auth = {'Authorization': 'Bearer ' + token['access_token']}
  payload = {
    'name': "Testes RD"
  }
  url = 'https://api.rd.services/marketing/account_info'
  response = requests.get(url, payload, headers=auth)
  return response.status_code == 200


def refresh(secret_path, token):
  url = 'https://api.rd.services/auth/token'
  payload = {
    'client_id': os.environ.get('RD_API_CLIENT_ID'),
    'client_secret':os.environ.get('RD_API_CLIENT_ID'),
    'refresh_token': token['refresh_token']
  }

  return requests.get(url, payload)