class VT:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a vt.my name is {self.name}. I used {self.age} generation.")

class TS:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a ts.my name is {self.name}. I used {self.age} generation.")

class IC:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a ic.my name is {self.name}. I used {self.age} generation.")

class MP:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a mp.my name is {self.name}. I used {self.age} generation.")
        
class AI:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a ai.my name is {self.name}. I used {self.age} generation.")
VA1=VT("vacuum tubes",1)
TS1=TS("transistors",2)
IC1=IC("integrated circuit",3)
MP1=MP("microprocessor",4)
AI1=AI("artificial inteligence",5)

for generation in(VA1,TS1,IC1,MP1,AI1):
    generation.info()
