from abc import ABC,abstractmethod
#Abstract class

class bank(ABC):
    def bank_info(self):
        print("welcoe to bank")


    @abstractmethod
    def interest(self):
        "abstract method"
        pass
    #sub class/child class of abstract class
class SBI(bank):
    def balance(self):
        print("balance is 100")
class sub(SBI):
    def interest(self):
        print("in sbi bank interest is 5 rupees")
s=sub()
s.bank_info()
s.balance()
s.interest()
    
