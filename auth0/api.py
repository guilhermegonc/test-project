import http.client
import os, json


def get_auth0_user(email):
    client_domain = os.environ.get('AUTH0_DOMAIN')
    client_id = os.environ.get('AUTH0_CLIENT_ID')
    client_secret = os.environ.get('AUTH0_CLIENT_SECRET')
    
    token = refresh_token(client_domain, client_id, client_secret)

    headers = {'authorization': f'Bearer {token}'}    
    conn = http.client.HTTPSConnection(client_domain)
    conn.request("GET", f'https://{client_domain}/api/v2/users?q=email:{email}&search_engine=v3', headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    data = data.decode('utf-8')
    data = json.loads(data)[0]

    return data

def refresh_token(domain, c_id, secret):
    conn = http.client.HTTPSConnection(domain)
    
    payload = f'{{"client_id":"{c_id}",'
    payload += f'"client_secret":"{secret}",'
    payload += f'"audience":"https://{domain}/api/v2/",'
    payload += f'"grant_type":\"client_credentials\"}}'

    headers = { 'content-type': "application/json" }
    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode('utf-8')
    data = json.loads(data)

    return data['access_token']
