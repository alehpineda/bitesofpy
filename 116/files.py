import os
import glob

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    return (filename for _, _, files in os.walk(dirname) 
            for filename in files if int(filename) >= size_in_kb*ONE_KB)


# Pybites solution
def get_files1(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    for file in glob.glob(os.path.join(dirname, '*')):
        if os.stat(file).st_size >= size_in_kb * ONE_KB:
            yield file
