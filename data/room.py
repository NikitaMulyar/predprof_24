import datetime

import sqlalchemy
from .db_session import SqlAlchemyBase


class Room(SqlAlchemyBase):
    __tablename__ = 'rooms'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    window_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __repr__(self):
        return f'<Room> {self.id} {self.number} {self.window_number}'
