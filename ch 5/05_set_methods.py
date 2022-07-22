# creating a empty set
b=set()
print(type(b))
# Adding the elements 
b.add(4)
b.add(5)
b.add(5) #adding same value is not work 
b.add(47)
b.add((4,5,8))

# b.add({4:5}) #Cannot adding List and dictionary in add
print(b)
##Lenthe of a set
print(len(b)) #Print the lenth of b set
##Remove an element
b.remove(5) #Remove 5 from the set b
# b.remove(15) #Throw an error while trying to remove 15 which is not present in the set

print(b)
print(b.pop())
print(b)

