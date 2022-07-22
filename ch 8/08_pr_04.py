# n*(n+1)/2

def add_num(num):
    if(num==1):
        return 1
    elif(num==0):
        return 0
    add=num+add_num(num-1)
    return add

num=int(input("Enter the number : "))
f=add_num(num)
print("The sum of first", num ,"natural number is : ",f)