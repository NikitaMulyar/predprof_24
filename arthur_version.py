import requests
import json
headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}
A = ["25-01-23","14-02-23","18-02-23","04-03-23","14-03-23","18-04-23","13-09-23","30-09-23","30-10-23"]
D = {}
for it in A:
    r = requests.get('https://olimp.miet.ru/ppo_it_final?day={}&month={}&year={}'.format(*it.split('-')), headers=headers).json()
    D[it] = r["message"]
s = input()  # Enter date



