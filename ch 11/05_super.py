class Person():
    country="India"
    def __init__(self):
        print("Initilitions Person ....\n")
        
    def TakeBreath(self):
        print("I am Breathing >>>>>")

class Employee(Person):
    company="Honda"
    def __init__(self):
        super().__init__()
        print("Initilitions Employee ....\n")

    def Getsalary(self):
        print("HE get salary $500/month")
    
    def TakeBreath(self):
        super().TakeBreath()
        print("I am Breathing >>>>> ++++++")

class Programmer(Employee):
    company="Fiver"
    
    def __init__(self):
        # super().__init__()
        print("Initilitions Progammer ....\n")

    def Getsalary(self):
        print("HE get salary $500/month")
    
    def TakeBreath(self):
        super().TakeBreath()
        print("I am Breathing >>>>>/////++++++")

# p=Person()
# p.TakeBreath()

# e=Employee()
# e.TakeBreath()

pr=Programmer()
# pr.TakeBreath()
