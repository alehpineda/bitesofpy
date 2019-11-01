from math import floor, ceil

def round_up_or_down(transactions, up=True):
   """Round the list of transactions passed in.
      If up=True (default) ronud up, else round down.
      Return a new list of rounded values
   """
   if up:
      return [ceil(transaction) for transaction in transactions]
   return [floor(transaction) for transaction in transactions]
