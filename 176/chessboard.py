WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
   """Create a chessboard with of the size passed in.
      Don't return anything, print the output to stdout"""
   size = int(size / 2)
   for _ in range(size):
      print((WHITE+BLACK)*size)
      print((BLACK+WHITE)*size)
