ATTRIBUTES = {
   'r':4,
   'w':2,
   'x':1,
   '-':0
}

THREE = 3

def _get_chunks(rwx: str, size:int = THREE):
   return (rwx[0+i:size+i] for i in range(0, len(rwx), size))

def _convert_octal(rwx: str) -> int:
   return sum(ATTRIBUTES[val] for val in rwx)

def get_octal_from_file_permission(rwx: str) -> str:
   """Receive a Unix file permission and convert it to
      its octal representation.

      In Unix you have user, group and other permissions,
      each can have read (r), write (w), and execute (x)
      permissions expressed by r, w and x.

      Each has a number:
      r = 4
      w = 2
      x = 1

      So this leads to the following input/ outputs examples:
      rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
      rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
      r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
   """

   user, group, other = _get_chunks(rwx)
   return f'{_convert_octal(user)}{_convert_octal(group)}{_convert_octal(other)}'


# Pybites solution
def get_octal_from_file_permission1(rwx: str) -> str:
   """Receive a Unix file permission and convert it to
      its octal representation.

      In Unix you have user, group and other permissions,
      each can have read (r), write (w), and execute (x)
      permissions expressed by r, w and x.

      Each has a number:
      r = 4
      w = 2
      x = 1

      So this leads to the following input/ outputs examples:
      rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
      rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
      r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
   """
   rwxs = '--- --x -w- -wx r-- r-x rw- rwx'.split()
   octals = [str(i) for i in range(0, 8)]
   permissions = dict(zip(rwxs, octals))

   parts = [rwx[i:i+3] for i in range(0, len(rwx), 3)]
   return ''.join(
      permissions[p]
      for p in parts
   )
