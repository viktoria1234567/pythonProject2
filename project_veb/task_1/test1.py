import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


def test_step1(user_login, post_title):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'}).json()['data']
    result_title = [i['title'] for i in result]
    assert post_title in result_title, 'test_step1 FAIL'


def test_step2(user_login, our_post_title):
    S.post(url=data['address'], headers={'X-Auth-Token': user_login},
                    data={'title': 'Котики', 'description': 'Красивый котик', 'content': 'Существует красивый котик'})
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}).json()['data']
    result_title = [i['description'] for i in result]
    assert our_post_title in result_title, 'test_step2 FAIL'
