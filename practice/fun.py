
def outer(func):
    def inner():
        func()
        print("hello buddy")
        
    return inner
f=outer
f()
#@outer
def wish():
    print('good morning')
wish()    

'''
def decor(func):
    def inner(a,b):
        func()
        result=a+b
        print(result)
    return inner
@decor
def add():
    print('result is:',)
add(10,20)
'''
g=(x for x in range(1,101) if x%5==0)
print(type(g))
for i in g:
    print(i,end=" ")
    