'''
def show(*n):
    for i in n:
        print(i)
        
show(10,20,30,40)
'''
'''
def show(a,b=20):
    print(a+b)
show(20,10)
'''
'''
def add(a,b):
    def inner():
       result=a+b
       return result
    i=inner()
    return i+5
    
a=add(10,20)
print(a)
'''
'''
def rec(n):
    if n==0:
        return 0
    else:
        res=n+rec(n-1)
    return res
    
print(rec(10))
'''
class duck:
    def show(self):
        print('duck class')
class dog:
    def show(self):
        print("dog class")
        
def myfunc(obj):
    obj.show()
list=[dog(),duck()]
for i in list:
    myfunc(i)
