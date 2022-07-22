My_Dict={
    "First":"In a  quick manner",
    "Suman":"A Coder",
    "marks":[1,25,44],
    "anotherdict":{'Suman':"player"},
    1:2
}

#Dictionary Methods
print(list(My_Dict.keys()))  #print the keys of the dictionary
print(My_Dict.values())  #print the values of the dictionary
print(My_Dict.items())  #print the (keys and values) for all contant of the dictionary
# Update the dictionary by adding keys-values
print(My_Dict)
update_dict={
    "Rahul":"Friend",
    "Varab":"Friend",
    "sulu":"Friend",
    "Suman":"a cricketer"
}
My_Dict.update(update_dict)

print(My_Dict)

print(My_Dict.get("Suman")) #Prints values associated with key "suman"
print(My_Dict["Suman"]) #Prints values associated with key "suman"
# Difference between .get and [] 
print(My_Dict.get("Suman2")) #throws an None as suman2 is not present in the Dictionary
print(My_Dict["Suman2"]) #throws an error as suman2 is not present in the Dictionary
