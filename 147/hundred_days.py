from datetime import date, timedelta
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    days = 0
    hundred = []
    while len(hundred) < 100:
        if (start_date + timedelta(days=days)).isoweekday() <= 5:
            hundred.append(start_date + timedelta(days=days))
        days += 1
    return hundred


# Pybites solution using dateutil
def get_hundred_weekdays1(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    date_range = rrule(DAILY, count=100,
                       byweekday=(MO, TU, WE, TH, FR),
                       dtstart=start_date)
    return [dt.date() for dt in date_range]
