import requests
import json
from tests.constants import HEADERS


def create_user(api_url, params):
    return requests.post(api_url, headers=HEADERS, data=json.dumps(params))


def get_all_users(api_url):
    return requests.get(api_url)


def get_user_by_id(api_url, user_id):
    return requests.get(f'{api_url}/{user_id}')
