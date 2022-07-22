def greater_fun(num1,num2,num3):
    if(num1>num2):
        big=num1
    else:
        big=num2

    if(big<num3):
        big=num3
    return big


num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))
b=greater_fun(num1,num2,num3)
print("The greatest number is : ",b)
