class p:
    def __init__(self):
        print('this is from parent class const')

    def m(self):
        print('this is from parent class method')

class c(p):
    def __init__(self):
        super().__init__()
        print('this is from child class const')

    def m(self):
        super().m()
        print('this is from child class method')

o=c().m()
       
    