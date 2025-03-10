class employee :
    def __init__(self):
        self.name=input("enter your name:")
        self.age=int(input("enter your age:"))
        self.email=input("enter your email:")
        self.designation=input("enter your designation")
        self.salary=int(input("enter your salary:"))

class temp(employee):
    def display(self):
        print("employee details are")
        print("name:",self.name)
        print("age:",self.age)
        print("email:",self.email)
        print("designation:",self.designation)
        print("salary:",self.salary)

obj1=temp()
obj1.display()
