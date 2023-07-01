import array as arr
l=[10,20,30,40,50]
a=arr.array('i',l)
a.append(100)
a.remove(10)
a.pop(1)
print(a)
print()

import numpy
l=[10,20,30,40,50]
n=numpy.array(l)
print(n)
print(type(n))
print()

from array import *
l=[10,20,30,40,50]
ar=array('i',l)
print(ar)