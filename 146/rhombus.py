STAR = '*'

def gen_rhombus(width):
  """Create a generator that yields the rows of a rhombus row
    by row. So if width = 5 it should generate the following
    rows one by one:

    gen = gen_rhombus(5)
    for row in gen:
      print(row)

    output:
          *
         ***
        *****
         ***
          *
  So the middle row is always equal to the width passed in. 
  Checkout how format or f-strings can help you here, 
  as well as the range builtin. Have fun!
  """
  list_1 = list(range(1, width + 1, 2))
  list_2 = list_1[::-1][1:]
  list_3 = list_1+list_2

  for i in list_3:
    row = STAR*i
    yield row.center(width, ' ')


# Pybites solution
def _print_row(i, width):
    return f'{STAR*i: ^{width}}'


def gen_rhombus1(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    # upper half
    for i in range(1, width+1, 2):
        yield _print_row(i, width)
    # lower half ('width-2' to not repeat middle row)
    for i in range(width-2, 0, -2):
        yield _print_row(i, width)