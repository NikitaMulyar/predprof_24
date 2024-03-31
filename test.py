import requests
import json

headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}

# 1 получаем даты
# r = requests.get('https://olimp.miet.ru/ppo_it_final/date', headers=headers)

# 2 получаем по дате
# r = requests.get('https://olimp.miet.ru/ppo_it_final?day=25&month=01&year=23', headers=headers)

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
# r = requests.post('https://olimp.miet.ru/ppo_it_final?day=25&month=01&year=23', headers=headers, data=payload)


A = ["25-01-23","14-02-23","18-02-23","04-03-23","14-03-23","18-04-23","13-09-23","30-09-23","30-10-23"]

D = {}

for it in A:
    #print(it.split('-'))
    r = requests.get('https://olimp.miet.ru/ppo_it_final?day={}&month={}&year={}'.format(*it.split('-')), headers=headers).json()
    #print(r["message"])
    D[it] = r["message"]

for it in D:
    print(it, D[it])

