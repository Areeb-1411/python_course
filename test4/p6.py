class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display(self):
        print(f"name {self.name},Age: {self.age},Grdae:{self.grade}")

n=input()
a=int(input())
g=input()

student=Student(n,a,g)
student.display()