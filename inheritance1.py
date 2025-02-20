class person:
    def __init__(self,name,age,classname):
        self.name=name
        self.age=age
        self.classname=classname
    def printing(self):
        print(self.name,self.age,self.classname)
class employee(person):
    def __init__(self,name,age,classname,company,dept,sal):
        super().__init__(name,age,classname)
        self.company=company
        self.dept=dept
        self.sal=sal    
    def printing(self):
        print(self.name,self.age,self.classname,self.company,self.dept,self.sal)        
obj=employee("arun",23,"bsc","zoho","developer",20000)
obj.printing()
