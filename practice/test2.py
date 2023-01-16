'''
def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result

f=fact(4)
print(f)
'''
'''
l="my string"
x=[i[0] for i in l if i !=" "]
print(x)
print(x[::-1])
'''
'''
list1 = [2, -7, 5, -64, -14]
count=0
cnt=0
for i in list1:
    if i>0:
        count += 1
    else:
        cnt += 1
print('positive numbers=',count)
print('negative numbers=',cnt)
'''
'''
a=[1,2,3,4]
b=[5,6,7,8]
c=zip(a,b)
print(list(c)) 
'''
# Get all tuple keys from dictionary
test_dict = {(5, 6) : 'gfg', (1, 2, 8) : 'is', (9, 10) : 'best'}

res = [ele for i in test_dict for ele in i ]
print(res)
