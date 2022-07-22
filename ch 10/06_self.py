class Employee:
    company="Google"
    def GetSalary(self):
        print(f"Salary of this employee working in {self.company} is {self.salary}")


harry=Employee()
harry.salary=100000
harry.GetSalary()  #= Employee.GetSalary(harry)
