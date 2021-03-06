from math import floor, ceil


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
      If up=True (default) ronud up, else round down.
      Return a new list of rounded values
   """
    return [ceil(t) if up else floor(t) for t in transactions]


# Pybites solution


def round_up_or_down1(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
   """
    func = ceil if up else floor
    return [func(t) for t in transactions]
