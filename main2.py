from funcs_back import *
from data import db_session
from db_funcs import *


if __name__ == "__main__":
    db_session.global_init('site.db')
    all_dates = get_all_dates()
    for date in all_dates:
        put_to_db_date()
    rooms()
