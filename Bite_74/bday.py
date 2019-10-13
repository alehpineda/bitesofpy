"""
Complete weekday_of_birth_date which takes a date object of a birthday and returns the corresponding weekday string.

For example Bob and Julian's birthdays return Saturday and Monday (that's why Bob is meant to relax and Julian to do all the work chuckle).

For this Bite you want to look at the datetime and calendar modules.
"""

import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    weekday = { 
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return weekday[calendar.weekday(date.year, date.month, date.day)]
