import datetime

from data import db_session
from data.window import Window


def make_matrix_for_front(date: datetime.datetime):
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
    return matrix
