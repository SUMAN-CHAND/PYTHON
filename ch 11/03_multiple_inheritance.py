class Employee():
    company="Visa"
    ecode=120

class FreeLinser():
    company="Fiver"
    lavel=0

    def Upgradelavel(self):
        self.lavel=self.lavel+1

class Programmer(FreeLinser,Employee):
    name="Rohit"

p=Programmer()
p.Upgradelavel()
print(p.lavel)
print(p.company)