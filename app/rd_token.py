import os
import boto3
import requests
import json
from .aws_connect import connect_to_s3


def get_valid_token():
  s3 = connect_to_s3()
  token = load_last_token(s3)
  token = token if is_valid(token) else refresh(token, s3)
  return {'Authorization': 'Bearer ' + token['access_token']}


def load_last_token(s3):
  response = s3.get_object(
      Bucket='test-project-production',
      Key='not-public/rd_api_token.json'
  )
  return json.load(response['Body'])


def is_valid(token):
  auth = {'Authorization': 'Bearer ' + token['access_token']}
  payload = {
    'name': "Testes RD"
  }
  url = 'https://api.rd.services/marketing/account_info'
  response = requests.get(url, payload, headers=auth)
  return response.status_code == 200


def refresh(token, s3):
  url = 'https://api.rd.services/auth/token'
  payload = {
    'client_id': os.environ.get('RD_API_CLIENT_ID'),
    'client_secret':os.environ.get('RD_API_CLIENT_ID'),
    'refresh_token': token['refresh_token']
  }
  token = requests.post(url, payload)
  token = token.json()
  update_s3(token, s3)
  
  return token

def update_s3(token, s3):
  response = s3.put_object(
    Bucket='test-project-production',
    Key='not-public/rd_api_token.json'
  )    
  pass