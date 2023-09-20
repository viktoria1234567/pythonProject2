import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


@pytest.fixture()
def user_login():
    result = S.post(url=data['url'], data={'username': data['login'], 'password': data['password']})
    response_json = result.json()
    token = response_json.get('token')
    return token


@pytest.fixture()
def post_title():
    return 'Новый пост'

@pytest.fixture()
def our_post_title():
    return 'Красивый котик'