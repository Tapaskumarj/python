'''
for i in range(5):
    if i==4:
        break
    print("you enterd:",i)
   '''
'''
i=1
while i<10:
    if i == 7:
        break
    print(i)  
    i+=1
'''
'''
n=5
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")

    for k in range(1*i+1):
        print("*",end=' ')
    print()
'''
'''
print('hello dude','good mrng',sep=':',end='@')
print('how r u')
'''
'''
for i in range(15):
    if i==10:
        continue
    print(i)
'''
s='tapas'
s1=','.join(reversed(s))
print(s1)