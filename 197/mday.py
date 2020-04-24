from datetime import date
from dateutil.relativedelta import relativedelta, SU


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
      is celebrated assuming it's the 2nd Sunday of May."""

    return date(year, 1, 1) + relativedelta(months=+4, weekday=SU(2))


# Pybites solution

MAY = 5


def get_mothers_day_date1(year):
    """Given the passed in year int, return the date Mother's Day
      is celebrated assuming it's the 2nd Sunday of May."""
    first_of_may = date(year=year, month=MAY, day=1)
    return first_of_may + relativedelta(weeks=1, weekday=SU)
