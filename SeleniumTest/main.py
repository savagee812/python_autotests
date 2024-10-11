import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1cc1674b13cd24a31740dc8b0e3fa72d'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN }

body_createpok = {
    "name": "Котозавр",
    "photo_id": 13
}

response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_createpok )

print(response.text)

pokemon_id = response.json()['id'] 

body_changenamepok = {
    "pokemon_id": pokemon_id,
    "name": "Kotik",
    "photo_id": 37 
}
body_catch = {
    "pokemon_id": pokemon_id
}

response_changenamepok = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_changenamepok )

print(response_changenamepok.text)

response_catch = requests.post(url= f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_catch )

print(response_catch.text)
