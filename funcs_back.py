import datetime

from data import db_session
from data.window import Window
from predprof_24.data.room import Room
from requests import get, post
import json


def make_matrix_for_windows(date: datetime.datetime):
    db_sess = db_session.create_session()
    ws = db_sess.query(Window).filter(Window.date == date).all()
    floors = {w.floor_number for w in ws}
    floors_num = len(floors)
    ws = {fl: sorted(list(filter(lambda w: w.floor_number == fl, ws)),
                     key=lambda w: (w.room_number, w.window_id)) for fl in floors}

    matrix = [[] for _ in range(floors_num)]

    floors = sorted(list(floors))
    for i in range(len(floors)):
        cur_fl = floors[i]
        for el in ws[cur_fl]:
            matrix[i].append((el.room_number, el.state))
    db_sess.close()
    return matrix


def make_matrix_for_rooms():
    db_sess = db_session.create_session()
    rooms = db_sess.query(Room).all()
    rooms = sorted(rooms, key=lambda r: (r.date, r.number))
    # Проверка корректности
    rooms = [[r.date, r.number, True] for r in rooms]
    db_sess.close()
    return rooms


def get_all_dates():
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}
    r = get('https://olimp.miet.ru/ppo_it_final/date', headers=headers).json()['message']
    return r


def get_data_by_day(day, month, year):
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}
    r = get(f'https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year % 100}', headers=headers).json()['message']
    return r


def post_correct_data(number_of_light_rooms, rooms, date: datetime.datetime):
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': 'ppo_10_11019'}
    payload = {
        "data": {
            "count": number_of_light_rooms,
            "rooms": sorted(rooms)
        },
        "date": date.strftime('%d-%m-') + date.strftime('%Y')[2:]
    }
    r = post('https://olimp.miet.ru/ppo_it_final/', headers=headers, data=payload).status_code
    return r


def rooms(json_response):
    kv = json_response["windows_for_flat"]["data"]
    rm = 0
    room = 0
    floor = 0
    rooms = []
    mnmp = {}
    for w in json_response["windows"]["data"]:
        floor += 1
        A = json_response["windows"]["data"][w]
        ind = 0
        for it in kv:
            room += 1
            now_kv = False
            mnmp[(floor, room)] = []
            for i in range(it):
                if A[ind]:
                    now_kv = True
                mnmp[(floor, room)].append(A[ind])
                ind += 1
            if now_kv:
                rm += 1
                rooms.append(room)
    mp = {"date": datetime.datetime.fromtimestamp(json_response["date"]["data"]), "all": room,  "turned_on": rm, "rooms": rooms, "windows": mnmp}
    return mp
