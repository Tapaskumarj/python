'''
a=['a','b','c']
b=[1,2,3]
c=dict(zip(a,b))
print(c)
'''
a=['a','b','c']
b=(1,2,3)
c=list(zip(a,b))
print(c)
for i in c:
    print(i)
