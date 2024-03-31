import datetime

import sqlalchemy
from .db_session import SqlAlchemyBase


class Date(SqlAlchemyBase):
    __tablename__ = 'dates'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Date> {self.date} {self.description}'
