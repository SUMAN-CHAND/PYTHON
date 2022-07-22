num1=int(input("Enter the 1 number : "))
num2=int(input("Enter the 2 number : "))
num3=int(input("Enter the 3 number : "))
num4=int(input("Enter the 4 number : "))

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2

else:
    f2=num3

if(f1>f2):
    print(f1,"Is greatest")
else:
    print(f2,"Is greatest")

