import requests
import time
import os

def fb_view_content(request):
    api_version = os.environ.get('FACEBOOK_API_VERSION')
    pixel_id = os.environ.get('FACEBOOK_PIXEL_ID')
    token = os.environ.get('FACEBOOK_TOKEN')
    url = f'https://graph.facebook.com/{api_version}/{pixel_id}/events?access_token={token}'
    
    ip = request.META.get('REMOTE_ADDR')
    agent = request.headers['User-Agent']
    payload = {
        "data": [
            {
                "event_name": "View Content",
                "event_time": time.time(),
                "action_source": "website",
                "user_data": {
                    "client_ip_address": ip,
                    "client_user_agent": agent
                }
            }
        ]
    }
    r = requests.post(url, params=payload)
    return
