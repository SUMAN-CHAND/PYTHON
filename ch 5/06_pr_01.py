
myDict={
    "jal":"water",
    "naun":"Salte",
    "darja":"Door"
}
print("Your option are : ",myDict.keys())
a=input("Enter the word which you want to know :")
# print("The meaning of your word is :",myDict[a])

#Below line never show any error if the key not present in the dictionary
print("The meaning of your word is :",myDict.get(a))


