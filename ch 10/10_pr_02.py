class Calculater:
    def square(self, num):
        self.num = num
        num_sqr = num * num
        return num_sqr

    def qube(self, num):
        self.num = num
        num_qube = num * num * num
        return num_qube
    
    def squ_root(self, num):
        self.num = num
        num_root =num **0.5
        return num_root


get_number = int(input("Enter the number which you want to square = "))
number1 = Calculater()
result = number1.square(get_number)
print(f"The result is {result}")

get_Qnumber = int(input("Enter the number which you want to Qube = "))
number2 = Calculater()
result2 = number2.qube(get_Qnumber)
print(f"The result is {result2}")

get_squroot = int(input("Enter the number which you want to Qube = "))
number3 = Calculater()
result3 = number3.squ_root(get_squroot)
print(f"The result is {result3}")

