#* * *
#* *
#*
def star_print(n):
    for i in range(n):
        print("* "*(n-i))
n=int(input("Enter the number lines : "))
star_print(n)