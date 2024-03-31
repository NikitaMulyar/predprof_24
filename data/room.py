import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Room(SqlAlchemyBase):
    __tablename__ = 'rooms'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)



    def __repr__(self):
        return f'<Window> {self.id} {self.date} {self.window_id}'
