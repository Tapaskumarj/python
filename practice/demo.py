'''
def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
print(fact(10))
'''
'''
l=[10,20,35,64,66]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
'''
'''
l=[10,20,35,64,66]
#l1=[10,20,35,64,66,94,65,97]
l2=list(map(lambda x,y:x+y,l))
print(l2)
'''
'''
name="tapas"
age=27
print(f"hello {name} and your age is{age}")
print("hello {} and your age is{}".format(name,age))
'''
'''
def show():
   l=input("enter a string:")
   s=set(l)
   for i in s:
       print(i,"occured",l.count(i),"times")
print(show.__doc__)
show()
'''
str1 = "tapas kumar jena"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)