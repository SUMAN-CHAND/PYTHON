sub1=int(input("Enter the first subject number : "))
sub2=int(input("Enter the second subject number : "))
sub3=int(input("Enter the third subject number : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("Fail! Because one of the subject number is less then 33%.")
elif(sub1+sub2+sub3)/3<40:
    print("Fail! Because total  number is less then 40%.")

else:
    print("Congatulations! You are pass.")
