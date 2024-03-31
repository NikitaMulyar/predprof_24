import requests

headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}
r = requests.get('https://olimp.miet.ru/ppo_it_final/date', headers=headers)
with open("file.json", "wt", encoding="utf8") as f:
    f.write(r.text)
print(r.text)