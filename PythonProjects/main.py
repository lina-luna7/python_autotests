import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = os.getenv('TRAINER_TOKEN')
print(TOKEN)
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "341595",
    "name": "Viii",
    "photo_id": 101
}
body_add_pokeboll = {
    "pokemon_id": "341595"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_add_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeboll)
print(response_add_pokeboll.text)

