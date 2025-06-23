import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv()

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = os.getenv('TRAINER_TOKEN')
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '36463'
NAME = 'LiLu'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_trainer_name():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response_get.json()["data"][0]["trainer_name"] == 'LiLu'


@pytest.mark.parametrize('key, value', [('trainer_name', 'LiLu'),('id', TRAINER_ID),('level', '5')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response_parametrize.json()["data"][0][key] == value