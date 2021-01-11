from ctypes import *
from ctypes.util import find_library

libc_location = find_library('c')
libc = cdll.LoadLibrary(libc_location)

print(libc.rand())
