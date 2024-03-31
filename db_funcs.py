import datetime

from data import db_session
from data.date import Date
from data.window import Window
from data.room import Room
from data.users import User


def put_to_db_date(date: datetime.datetime, description):
    db_sess = db_session.create_session()
    d = Date(date=date, description=description)
    res = db_sess.query(Date).filter(Date == d).first()
    if res:
        db_sess.close()
        return 'Такая дата уже есть'
        return
    db_sess.add(d)
    db_sess.commit()
    db_sess.close()
    return 'Дата успешно добавлена'


def put_to_db_windows(date: datetime.datetime, states, floor_number, room_number):
    db_sess = db_session.create_session()
    for i, el in enumerate(states):
        w = Window(date=date, state=el, floor_number=floor_number, room_number=room_number, window_id=i)
        res = db_sess.query(Window).filter(Window == w).first()
        if res:
            continue
        db_sess.add(w)
    db_sess.commit()
    db_sess.close()
    return 'Окна успешно добавлены'


def put_to_db_room(date: datetime.datetime, number, window_number):
    db_sess = db_session.create_session()
    r = Room(date=date, number=number, window_number=window_number)
    res = db_sess.query(Room).filter(Room == r).first()
    if res:
        db_sess.close()
        return 'Такая комната уже есть'
    db_sess.add(r)
    db_sess.commit()
    db_sess.close()
    return 'Комната успешно добавлена'


def put_to_db_user(login, password, name, surname):
    db_sess = db_session.create_session()
    if db_sess.query(User).filter(User.login == login).first():
        db_sess.close()
        return 'Такой пользователь уже есть'
    user = User(
        name=name,
        login=login,
        surname=surname
    )
    user.set_password(password)
    db_sess.add(user)
    db_sess.commit()
    db_sess.close()
    return 'Регистрация успешна'
