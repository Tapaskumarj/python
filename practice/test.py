'''
import pr1 as p
p.add(30,40)
print(__name__)
#print(dir())
'''
'''
for i in range(0,20):
    print('*',end=' ')
'''
#number of occurrences in a string
def count():
    st=input("enter a string:")
    s=set(st)
    for i in s:
        print(i,"occurs",st.count(i),"times")
count()