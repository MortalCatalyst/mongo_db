import datetime

BASE = datetime.datetime(2017, 1, 1)


def dates_range(max_date, min_date):
    date_list = [
        BASE - datetime.timedelta(days=x) for x in range(max_date, min_date)
    ]
    return date_list


DATE_VALUES = dates_range(-210, 0)


def date_day(daytocheck):
    """
    get a date from the generator
    confirm if its saturday.
    """
    my_saturdays = []
    for day in DATE_VALUES:
        if day.weekday() == daytocheck:
            my_saturdays.append(day)
    return my_saturdays


LIST_OF_DATES = date_day(5)
