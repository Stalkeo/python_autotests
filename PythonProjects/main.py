import requests
import json

token = '27100115fcfe2ddc7815f101dc15df2d'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token' : token}, json={
    "name": "Даня",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response.text)
pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token': token}, json={
    "pokemon_id": pokemon_id,
    "name": "ДаняТест",
    "photo": ""
})
print(response_change.text)

response_addpokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'trainer_token' : token}, json={
    "pokemon_id": pokemon_id
    
})
print(response_addpokeball.text)
