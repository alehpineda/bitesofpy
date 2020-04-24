"""
In this Bite you learn how to lookup values from a dictionary or in 
Python: dict.

You are presented with workout_schedule with keys: days and values: 
workouts. Complete get_workout_motd that receives a day string, 
title case it so the function can receive case insensitive days, 
look it up in the dict and do two things:

If the day (key) is not in the dictionary, raise a KeyError, we 
don't want this function to continue, the caller needs to catch 
this exception,

If the key is in the dictionary, return chill or go_train depending 
if it's a Rest day or not. The latter you will need to 
string-interpolate using format.
"""

workout_schedule = {
    "Friday": "Shoulders",
    "Monday": "Chest+biceps",
    "Saturday": "Rest",
    "Sunday": "Rest",
    "Thursday": "Legs",
    "Tuesday": "Back+triceps",
    "Wednesday": "Core",
}
rest, chill, go_train = "Rest", "Chill out!", "Go train {}"


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       Then check if this title cased day is in the given workout_schedule dict.

       If it is retrieve the workout (value), if not raise a KeyError.

       Return the chill variable if it's a rest day (Saturday / Sunday),
       else return the go_train variable with the workout interpolated.

       Examples:
       - if day is Saturday -> return 'Chill out!'
       - if day is Thursday -> return 'Go train Legs'
       - if day is Sunday -> return 'Chill out!'
       - if day is Monday -> return 'Go train Chest+biceps'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    if workout_schedule[day.lower().capitalize()]:
        if workout_schedule[day.lower().capitalize()] == rest:
            return chill
        else:
            return go_train.format(workout_schedule[day.lower().capitalize()])
    else:
        raise KeyError
