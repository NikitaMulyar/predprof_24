import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Window(SqlAlchemyBase):
    __tablename__ = 'windows'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    window_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    state = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    room_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    floor_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __repr__(self):
        return f'<Window> {self.id} {self.date} {self.window_id}'
