import calendar
from datetime import date, datetime, timedelta

import pytz
from dateutil.relativedelta import relativedelta


def add_months(start_date, months):
    month = start_date.month + months - 1
    year = start_date.year + (month // 12)
    month = (month % 12) + 1
    day = min(start_date.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def get_leap_year_days(start_date, end_date):
    """
    number of leap days in the given year
    :param start_date:
    :param end_date:
    :return: Number of days
    """
    days = 0
    for year in range(start_date.year, end_date.year + 1):
        if calendar.isleap(year):
            leap_day = date(year, 2, 29)
            if (leap_day >= start_date) and (leap_day <= end_date):
                days += 1
    return days


def get_future_date(days=0, months=0, years=0, date_format="%Y-%m-%d", start_date=None):
    if not start_date:
        start_date = datetime.today()
        if all(v == 0 for v in [years, months, days]):
            years = 1
        return (start_date + relativedelta(years=years, months=months, days=days)).strftime(date_format)


def get_todays_date(date_format="%Y-%m-%d", time_zone="US/Pacific"):
    """
    get the current date and convers to a string, return the string
    :param date_format:
    :param time_zon:
    :return:
    """
    return datetime.now(pytz.timezone(time_zone)).strftime(date_format)


def get_date_isoformat(str_date, from_format="%Y-%m-%d"):
    """
    Converts given date to Iso format from format provided
    :param start_date:
    :param from_format:
    :return:
    """
    return datetime.strptime(str_date, from_format).date().isoformat()


def get_date_range(start_date, end_date):
    """

    :param start_date:
    :param end_date:
    :return: list of dates representing the days between start_date and end_date
    """
    return (start_date + timedelta(days=i)
            for i in range(0, (end_date - start_date).days + 1, 1))


print(add_months(date.today(), 12))
print(get_future_date(days=1, months=1, years=1))
print(get_date_isoformat(str(date.today())))
print("------------")
for day in get_date_range(date.today(), add_months(date.today(), months=1)):
    print(day)

