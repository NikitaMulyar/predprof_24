from funcs_back import *
from data import db_session
from db_funcs import *
import pprint

if __name__ == "__main__":
    db_session.global_init('db/site.db')
    all_dates = get_all_dates()
    for date in all_dates:
        date = date.split('-')
        date[-1] = '20' + date[-1]
        date = "-".join(date)
        date = datetime.datetime.strptime(date, "%d-%m-%Y")
        put_to_db_date(date=date, description='')
        res = rooms(get_data_by_day(date.day, date.month, date.year))
        for w in res['windows']:
            put_to_db_windows(date, res['windows'][w], w[0], w[1])
            put_to_db_room(date, w[1], len(res['windows'][w]))
        pprint.pprint(make_matrix_for_windows(date))
