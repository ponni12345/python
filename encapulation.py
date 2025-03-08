
class student:
    def __init__(self,name):
        self.name=name
    def gettername(self):
        print(self.name)
    def settername(self,name):
        self.name=name

st1=student("steave")
st1.gettername()
st1.settername("harish")
st1.gettername()


class student:
    def __init__(self,name,age,classname):
        self.name=name
        self.age=age
        self.classname=classname
    def printing(self):
        print(self.name,self.age,self.classname)
    def gettername(self):
        print(self.name)
        print(self.age)
        print(self.classname)
    def settername(self,name,age,classname):
        self.name=name
        self.age=age
        self.classname=classname

st1=student("arun",23,"mba")
st1.gettername()
st1.settername("raj",24,"bsc")
st1.gettername()
