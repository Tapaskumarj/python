def decor(func):
    def inner(name):
        if name =='tapas':
            print('hello',name,'good morning')
        else:
            func(name)
    return inner

@decor
def show(name):
    print('hello',name,'how are you')

show('tapas')
show('sumit')