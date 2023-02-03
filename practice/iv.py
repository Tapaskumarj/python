a=[1,2,3,4,5]
from functools import reduce
l=reduce(lambda x,y:x+y,a)
print(l)