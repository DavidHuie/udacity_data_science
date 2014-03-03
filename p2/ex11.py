import datetime
import time


def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-date.

    In order to join these two data sets together, we'll want the dates
    formatted the same way.  Write a function that takes as its input
    a date in the MTA Subway data format, and returns a date in the
    weather underground format.

    Hint:
    There is a useful function in the datetime library called strptime.
    More info can be seen here:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''
    t = time.strptime(date, '%m-%d-%y')
    d = datetime.datetime(*t[:6])
    return d.strftime('%y-%m-%d')
