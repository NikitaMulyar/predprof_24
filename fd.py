import requests
A = ["25-01-23","14-02-23","18-02-23","04-03-23","14-03-23","18-04-23","13-09-23","30-09-23","30-10-23"]

headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}

for it in A:
    print(it.split('-'))
    r = requests.get('https://olimp.miet.ru/ppo_it_final?day={}&month={}&year={}'.format(*it.split('-')), headers=headers)


    r.encoding = "utf-8"
    with open("file.json", "wt", encoding="utf8") as f:
        f.write(r.text)
    print(r.text)
