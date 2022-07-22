
class Employee():
    company="Google"

    def showDetail(self):
        print("This is a Employee")

class Programmer(Employee):
    language="Python"
    # company="YouTube"

    def getLanguage(self):
        print(f"He Working in {self.language}")

    def showDetail(self):
        print("This is a Programmer")

e=Employee()
e.showDetail()
p=Programmer()
p.showDetail()
print(e.company)
print(p.company)
print(p.language)