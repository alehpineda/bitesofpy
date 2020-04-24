"""
In this bite you will work with a list of names.

First you will write a function to take out duplicates 
and title case them.

Then you will sort the list in alphabetical descending 
order by surname and lastly determine what the shortest 
first name is. For this exercise you can assume there 
is always one name and one surname.

With some handy Python builtins you can write this in 
a pretty concise way. Get it sorted :)
"""

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    # return a list of a dict keys
    # by rule the keys of a dict are unique
    # list comprehension
    # title() capitalize all the words and lowers
    # the rest
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # Sorted has a key parameter that can be modified
    # sorted by int, len, reverse it, or use a lambda
    # sorted return a copy of the list
    return sorted(names, reverse=True, key=lambda x: x.split()[-1])


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # List comprehension
    names = [name.split()[0] for name in names]
    # min and max also have a key parameter
    return min(names, key=len)
