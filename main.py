## Задание №1
# import requests
#
# heroes_data = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json').json()
# heroes = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes_data))
# int_dict = {hero['name']:hero['powerstats']['intelligence'] for hero in heroes}
#
# print('Самый умный супергерой:')
# print(max(int_dict, key=int_dict.get))

## Задание №2
import requests

class ya:
    