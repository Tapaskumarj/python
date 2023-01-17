'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
l=zip(keys,values)
d=dict(l)
print(d)
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)