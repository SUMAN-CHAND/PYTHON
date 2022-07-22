class Employee:
    company="Google"

    def __init__(self,name,salary,subunit):
        self.name =name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
        
    def GetSalary(self,signature):
        print(f"Salary of this employee working in {self.company} is {self.salary} \n {signature}")
    @staticmethod
    def greet():
        print("Good Morning")

    @staticmethod
    def time():
        print("Time is 9 am at morning.")

harry=Employee("Harry",100,"YouTube")
# harry=Employee() --> This throws an error 
harry.getDetails()