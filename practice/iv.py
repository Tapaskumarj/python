class duck:
    def walk(self):
        print('duck class')
        
class dog:
    def walk(self):
        print('dog class')
        
def show(obj):
    obj.walk()
d=duck()
show(d)