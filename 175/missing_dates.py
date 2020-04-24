import pandas as pd


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
        of missing datetime.date objects (no worries about order).

        You can assume that the first and last date of the
        range is always present (assumption made in tests).

        See the Bite description and tests for example outputs.
    """
    # .date converts from DatetimeIndex to a list of datetime.date objects
    all_dates = pd.date_range(start=min(dates), end=max(dates)).date
    return set(all_dates) - set(dates)


# Pybites solution

from dateutil import rrule


def get_missing_dates1(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    start = min(dates)
    count = max(dates).day - start.day
    date_range = [
        d.date() for d in rrule.rrule(rrule.DAILY, count=count, dtstart=start)
    ]
    return set(date_range) - set(dates)
