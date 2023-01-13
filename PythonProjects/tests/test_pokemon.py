import requests
import pytest

token = '27100115fcfe2ddc7815f101dc15df2d'

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200
    print(response.status_code)

def test_trainer_id():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1754'})
    assert response.json()['trainer_name'] == 'Даня'
    print(response)