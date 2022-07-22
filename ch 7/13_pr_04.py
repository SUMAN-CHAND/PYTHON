
# User input
num=int(input("Enter a number which you want to cheak : "))

flag=False

if num>1:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
if flag:
    print(num,"is not a Prime number")
else:
    print(num,"is a Prime number")
