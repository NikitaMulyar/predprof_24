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


def rooms(json_response):
    kv = json_response["message"]["windows_for_flat"]["data"]
    rm = 0
    room = 0
    rooms = []
    for w in json_response["message"]["windows"]["data"]:
        A = json_response["message"]["windows"]["data"][w]
        ind = 0
        for it in kv:
            now_kv = False
            for i in range(it):
                if A[ind]:
                    now_kv = True
                ind += 1
            room += 1
            if now_kv:
                rm += 1
                rooms.append(room)
    mp = {"len": rm, "rooms": rooms, "data": datetime.fromtimestamp(json_response["message"]["date"]["data"]).strftime("%Y-%m-%d")}
    return mp


print(rooms(json_response))