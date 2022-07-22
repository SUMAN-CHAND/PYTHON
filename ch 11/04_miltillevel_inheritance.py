class Person():
    country="India"

    def TakeBreath(self):
        print("I am Breathing >>>>>")

class Employee(Person):
    company="Honda"

    def Getsalary(self):
        print("HE get salary $500/month")
    
    def TakeBreath(self):
        print("I am Breathing >>>>> ++++++")

class Programmer(Employee):
    company="Fiver"

    def Getsalary(self):
        print("HE get salary $500/month")
    
    def TakeBreath(self):
        print("I am Breathing >>>>>/////++++++")

p=Person()
p.TakeBreath()
e=Employee()
print(e.company)
e.TakeBreath()
pr=Programmer()
pr.TakeBreath()
print(pr.country)
