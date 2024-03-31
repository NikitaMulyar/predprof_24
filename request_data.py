import requests
import json

headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}
# 1 получаем даты
# r = requests.get('https://olimp.miet.ru/ppo_it_final/date', headers=headers).json()

# 2 получаем по дате
r = requests.get('https://olimp.miet.ru/ppo_it_final?day=25&month=01&year=23', headers=headers).json()

# 3 запрос проверки
# payload = """{
# 	"data": {
# 		"count": 4,
# 		"rooms": [
# 			3,
# 			5,
# 			9,
# 			10
# 		]
# 	},
# 	"date": "25-01-23"
# }"""
# r = requests.post('https://olimp.miet.ru/ppo_it_final?day=25&month=01&year=23', headers=headers, data=payload).json()

json.dump(r, open('file.json', 'w'))
