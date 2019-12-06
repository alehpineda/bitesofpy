import pandas as pd

def get_missing_dates(dates):
   """Receives a range of dates and returns a sequence
      of missing datetime.date objects (no worries about order).
      
      You can assume that the first and last date of the
      range is always present (assumption made in tests).

      See the Bite description and tests for example outputs.
   """
   start, *_, end = sorted(dates)
   complete_dates = pd.date_range(start=start, end=end).date
   return list(set(dates) ^ set(complete_dates))
