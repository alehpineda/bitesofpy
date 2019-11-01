import os


def count_dirs_and_files(directory='.'):
   """Count the amount of of directories and files in passed in "directory" arg.
      Return a tuple of (number_of_directories, number_of_files)
   """
   files = folders = 0

   for _, dirnames, filenames in os.walk(directory):
      files += len(filenames)
      folders += len(dirnames)
   
   return (folders, files)
