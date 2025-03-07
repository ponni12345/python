from abc import ABC,abstractmethod
#Abstract class

class bank(ABC):
    def bank_info(self):
        print("welcome to deepak")


    @abstractmethod
    def interest(self):
        "abstract method"
        pass
    #sub class/child class of abstract class
class deepak(bank):
    def balance(self):
        print("your balance is 1000")
class sub(deepak):
    def interest(self):
        print("In sbi bank interest is 5 rupees")
s=sub()
s.bank_info()
s.balance()
s.interest()
    
