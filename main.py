import requests
token = '3afcb6855cb091598df77545b22c2b56'
createpok = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
     json=
     {
     "name": "Pytest",
     "photo": "https://dolnikov.ru/pokemons/albums/010.png"
     })
print(createpok.text)

renamepok = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
     json=
     {
    "pokemon_id": 6302,
    "name": "PytestRename",
    "photo": ""
})
print(renamepok.text)

catchpok = requests.post('https://pokemonbattle.me:9104//trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token': token},
     json=
     {
    "pokemon_id": 6302
})
print(catchpok.text)