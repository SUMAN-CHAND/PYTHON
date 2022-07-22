class Employee():
    company="Google"
    salary=100
suman=Employee()
rahul=Employee()
suman.salary=300
rahul.salary=410
print(suman.company)
print(rahul.company)

Employee.company="YouTube"
print(suman.company)
print(rahul.company)

print(suman.salary)
print(rahul.salary)