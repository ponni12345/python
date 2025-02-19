class student:
    def getdetails(self,name,age,college,dept):
        self.name=name
        self.age=age
        self.college=college
        self.dept=dept

    def show(self):
        print(f"hi this is {self.name},age is {self.age},{self.dept}-{self.college}")

bala=student()
bala.getdetails("bala",24,'prist','b.sc')
bala.show()
