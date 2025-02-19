class employee:
    def getdetails(self,name,age,company,job,salary):
        self.name=name
        self.age=age
        self.company=company
        self.job=job
        self.salary=salary
    def show(self):
        print(f"hi this is {self.name},age is {self.age},{self.job}-{self.company},the salary {self.salary}")

bala=employee()
bala.getdetails("arun",24,'zoho','tester',20000)
bala.show()

bala=employee()
bala.getdetails("deepak",23,'cisco','software developer',25000)
bala.show()

bala=employee()
bala.getdetails("raj",25,'google','accountant',30000)
bala.show()

bala=employee()
bala.getdetails("viji",24,'microsoft','engineer',35000)
bala.show()

bala=employee()
bala.getdetails("narmatha",23,'IBM','manager',20000)
bala.show()






