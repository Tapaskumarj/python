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
