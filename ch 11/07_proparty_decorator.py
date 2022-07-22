class Employee():
    company="Cemal"
    salary=5000
    salaryBonas=540
    # totalSalary=5500
    @property
    def totalSalary(self):
        return self.salary+self.salaryBonas

    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonas=val-self.salary

e=Employee()
print(e.totalSalary)
e.totalSalary=5200
print(e.salary)
print(e.salaryBonas)