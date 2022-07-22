import secrets 
# ******snake water gun ******  ******rock paper scissors****  

def snake_water_gun(you,comp):
    # pass
    if(comp==you):
        return None
    elif(comp=='s'):
        if(you=='w'):
            return False
        elif(you=='s'):
            return True
    elif(comp=='w'):
        if(you=='g'):
            return False
        elif(you=='s'):
            return True
    elif(comp=='g'):
        if(you=='s'):
            return False
        elif(you=='w'):
            return True


    

# print("Enter 's'for snake,'w' for water & 'g' for gun  :  ")
you=input("Enter 's'for snake,'w' for water & 'g' for gun  : ")

comp_rendom=secrets.randbelow(100)
# print(comp)
if(comp_rendom<33):
    comp='s'
elif(comp_rendom<66):
    comp='w'
elif(comp_rendom<100):
    comp='g'

# print(comp)

result=snake_water_gun(you,comp)

print(f"Computer chose : {comp}")
print(f"You chose : {you}")

if(result==None):
    print("The game is Draw")
elif result:
    print("You Won the game!")
else:
    print("You Loss!")


