import random
n= random.randint(1,100)
print(n)
userguess=None
guesses=0

while (userguess!=n):
    userguess=int(input("Enter Your predict: "))
    guesses+=1
    if userguess==n:
        print("Your Guess is right!")
    else:
        if userguess>n:
            print("Your Guess is high. Please Enter lower number!")
        else:
            print("Your Guess is low. Please Enter higher number!")


print(f"You guess the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
if hiscore>guesses:
    print("******You broke the high score!******")
    with open("hiscore.txt","w") as f:
        f.write (str(guesses))


        
# ****This is a nubber guessing game ******
# suman chand
