import requests
import json

# Create your tests here.
BASE_URL = 'http://127.0.0.1:8000/'
END_URL = 'bhojan_api/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data:{
            'id':id
        }
    resp = requests.get(BASE_URL+END_URL,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource()
