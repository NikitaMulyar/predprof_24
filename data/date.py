import sqlalchemy
from .db_session import SqlAlchemyBase


class Date(SqlAlchemyBase):
    __tablename__ = 'dates'

    date = sqlalchemy.Column(sqlalchemy.DateTime, primary_key=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Date> {self.date} {self.description}'
