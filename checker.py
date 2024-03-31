import requests
import json
import fg
from datetime import datetime

false = False
true = True

json_response = {"message": {"date": {"data": 1674594000,
                                      "description": "\u0422\u0430\u0442\u044c\u044f\u043d\u0438\u043d \u0434\u0435\u043d\u044c"},
                             "flats_count": {"data": 3,
                                             "description": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043d\u0430\u0442 \u043d\u0430 \u044d\u0442\u0430\u0436\u0435"},
                             "windows": {"data": {"floor_1": [false, true, false, true, false, false],
                                                  "floor_2": [true, false, true, false, false, true],
                                                  "floor_3": [false, false, true, false, true, false],
                                                  "floor_4": [false, false, false, true, false, true]},
                                         "description": "\u041e\u043a\u043d\u0430 \u043f\u043e \u044d\u0442\u0430\u0436\u0430\u043c, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0433\u043e\u0440\u0438\u0442 \u0441\u0432\u0435\u0442"},
                             "windows_for_flat": {"data": [3, 2, 1],
                                                  "description": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u043a\u043e\u043d \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0438\u0437 \u043a\u043e\u043c\u043d\u0430\u0442 \u043d\u0430 \u044d\u0442\u0430\u0436\u0435 \u0441\u043b\u0435\u0432\u0430 \u043d\u0430\u043f\u0440\u0430\u0432\u043e"}}}


def check(json_response):
    mp = fg.rooms(json_response)

    dat = mp["date"].strftime("%d-%m-") + mp["date"].strftime("%Y")[2:]
    print(dat)

    headers = {"Content-Type": "application/json", "X-Auth-Token": "ppo_10_21931"}
    payload = {
        "data": {
            "count": mp["turned_on"],
            "rooms": mp["rooms"]
        },
        "date": dat
    }
    r = requests.post('https://olimp.miet.ru/ppo_it_final', headers=headers, data=payload).json()
    #print(r)
    #json.dump(r, open('file.json', 'w'))
    return r == r



if __name__ == "__main__":
    check(json_response)