class Programmer:
    company="Microsoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product
    
    def getInfo(self):
        print(f"The name of the employee is {self.name} and the product is {self.product}")


suman=Programmer("Suman",'Github')
suman1=Programmer("Suman1",'phone')

suman.getInfo()
suman1.getInfo()