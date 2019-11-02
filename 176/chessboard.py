WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
   """Create a chessboard with of the size passed in.
      Don't return anything, print the output to stdout"""
   size = int(size / 2)
   for _ in range(size):
      print((WHITE+BLACK)*size)
      print((BLACK+WHITE)*size)


# Pybites solution


def create_chessboard1(size=8):
   """Create a chessboard with of the size passed in.
      Don't return anything, print the output to stdout"""
   board = ''

   for i in range(size):
      for j in range(size):
         if (i + j) % 2 == 0:
            board += ' '
         else:
            board += '#'
      board += '\n'

   print(board)
