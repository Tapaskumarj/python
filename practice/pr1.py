'''def add(a,b):
    sum=a+b
    c= print ('the sum is:',sum)
add(10,20)
print(__name__)
print(dir())
'''
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + 5

    return inner_fun(a, b)
    

result = outer_fun(5, 10)
print(result)