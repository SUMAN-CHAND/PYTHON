class Employee():
    company="Google"
    salary=100
suman=Employee()
rahul=Employee()

# creating instance attribute for both object
# suman.salary=300
# rahul.salary=410
suman.salary=50

print(suman.salary)
print(rahul.salary)

# below line throws an error as address is not present in the instance/class
# print(rahul.address)