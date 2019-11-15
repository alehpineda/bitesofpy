def generate_xmas_tree(rows=10):
   """Generate a xmas tree of stars (*) for given rows (default 10).
      Each row has row_number*2-1 stars, simple example: for rows=3 the
      output would be like this (ignore docstring's indentation):
      *
      ***
      *****"""
   xmas = []
   
   for row in range(1, rows+1):
      space = (rows - row)*' '
      xmas.append(space+(row*2-1)*'*')

   return '\n'.join(xmas)


# Pybites solution

def generate_xmas_tree1(rows=10):
   """Generate a xmas tree of stars (*) for given rows (default 10).
      Each row has row_number*2-1 stars, simple example: for rows=3 the
      output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
   width = rows*2
   output = []

   for i in range(1, width+1, 2):
      row = '*'*i
      output.append(row.center(width, ' '))

   return '\n'.join(output)
