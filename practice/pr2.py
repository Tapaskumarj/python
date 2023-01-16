class student:
    def __init__(self):
        self.name='tapas'
        self.age=27
        self.marks=95
    
    def show(self):
        print("your name is:",self.name)
        print("your age is:",self.age)
        print("your marks are:",self.marks)

s=student()
s.show()