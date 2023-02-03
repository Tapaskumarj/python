def mygen(n):
    for i in range(1,n+1):
        yield i
a=mygen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))