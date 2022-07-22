num=int(input("Enter a number : "))

for i in range(num):
    print(" " * (num-i-1) ,end="")
    print("*" * (2*i+1), end="")
    print(" " * (num-i-1))
   


# end=""  is use to no new line after a line execute
