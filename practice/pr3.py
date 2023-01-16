'''
for i in range(102):
    if i %2 != 0:
        print(i)
'''
'''
dict={'a':1,'b':2,'c':3}
#x=[*dict]
x=dict.keys()
print(x)
'''
'''
i=1
while i<=15:
    print(i)
    i+=1
'''
'''
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
a.extend(b)
#d.extend(c)
print(a)
print(b)
'''
l=range(1,101)
l1=[i for i in l if i%5==0 ]
print(l1)