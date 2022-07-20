import requests

def superhero_api(name_one, name_two, name_three):
    url = f'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()
    superHero = []
    for id in response:
        if id['name'] == name_one or id['name'] == name_two or id['name'] == name_three:
            superHero.append(id)
    id_superHero = 0
    intelligence = 0
    for sample in superHero:
        url = f'https://akabab.github.io/superhero-api/api/powerstats/{str(sample["id"])}.json'
        response = requests.get(url).json()
        if response['intelligence'] > intelligence:
            intelligence = response['intelligence']
            id_superHero = str(sample['id'])
    url = f'https://akabab.github.io/superhero-api/api/id/{id_superHero}.json'
    response = requests.get(url).json()
    print(f'Cамый умный (intelligence) из трех супергероев - {response["name"]}, его значение intelligence '
          f'равно {response["powerstats"]["intelligence"]}')


if __name__ == '__main__':
    superhero_api(name_one="Hulk", name_two="Captain America", name_three="Thanos")
