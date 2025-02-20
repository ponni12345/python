class person:
    def __init__(self,name,age,classname):
        self.name=name
        self.age=age
        self.classname=classname
    def printing(self):
        print(self.name,self.age,self.classname)
class student(person):
    def __init__(self,name,age,classname,dept,year):
        super().__init__(name,age,classname)
        self.dept=dept
        self.year=year
    def printing(self):
        print(self.name,self.age,self.classname,self.dept,self.year)

obj=student("harish",23,"mba","mba",2)
obj.printing()
        
