class Employee():
    company="Cemal"
    salary=100
    location="Delhi"

    # def changeSalary(self,sel):
    #     self.__class__.salary=sel
    @classmethod  
    def changeSalary(cls,sel):
        cls.salary=sel


e=Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)

print(Employee.salary)