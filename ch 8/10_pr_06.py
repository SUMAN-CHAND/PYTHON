
def change(inch):
    cm = inch * 2.54
    return cm  

inch=float(input("Enter the value of inches : "))
f=change(inch)
print("The value of cm is : ",f)