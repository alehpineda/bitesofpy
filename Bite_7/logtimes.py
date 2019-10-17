"""
In this bite we will look at this small server log finding the first 
and last system shutdown events:

INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.
You need to calculate the time between these two events. First extract 
the timestamps from the log entries and convert them to datetime 
objects. Then use datetime.timedelta to calculate the time difference 
between them.

You can assume the logs are sorted in ascending order. Check out the 
docstrings and the TESTS for more info.

Good luck and keep calm and code in Python!
"""

from datetime import datetime
import os
import urllib.request
from tempfile import gettempdir

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
TMP = gettempdir()
logfile = os.path.join(TMP, 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    timestamp = line.split()[1]
    date_str = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(timestamp, date_str)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown = [convert_to_datetime(line) for line in loglines 
                if SHUTDOWN_EVENT in line]
    
    return shutdown[-1] - shutdown[0]
