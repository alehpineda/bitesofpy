PYBITES = "pybites"


def convert_pybites_chars1(text):
   """Swap case all characters in the word pybites for the given text.
      Return the resulting string."""
   swap_case = []
   for char in text:
      if char.lower() in PYBITES:
         swap_case.append(char.swapcase())
      else:
         swap_case.append(char)
   
   return "".join(swap_case)


# [f(x) if condition else g(x) for x in sequence]
# [f(x) for x in sequence if condition]
def convert_pybites_chars(text):
   """Swap case all characters in the word pybites for the given text.
      Return the resulting string."""
   return "".join(char.swapcase() if char.lower() in PYBITES 
      else char for char in text)
