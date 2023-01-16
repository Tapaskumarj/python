class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def talk(self):
        print("your name is:",self.name)
        print("your age is:",self.age)
        print("your marks are:",self.marks)

s=student('tapas',27,92)
s.talk()
print(s.name)