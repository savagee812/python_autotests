import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1cc1674b13cd24a31740dc8b0e3fa72d'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = '6870'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
    assert response.status_code ==200

    def test_part_of_response():
        response_get = response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
        assert response_get.json()["data"][0]["name"] == 'Kotik'