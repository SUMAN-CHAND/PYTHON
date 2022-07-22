class Employee:
    company="Google"
    def GetSalary(self,signature):
        print(f"Salary of this employee working in {self.company} is {self.salary} \n {signature}")
    @staticmethod
    def greet():
        print("Good Morning")

    @staticmethod
    def time():
        print("Time is 9 am at morning.")
harry=Employee()
harry.salary=100000
harry.GetSalary("Thanks!")  #= Employee.GetSalary(harry)
harry.greet()  #Employee.greet()
harry.time()