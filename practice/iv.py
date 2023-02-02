s=input("enter a string:")
s1=set(s)
for i in s1:
    print('the letter',i,'is situated',s.count(i),'times')