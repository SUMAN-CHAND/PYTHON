
text=input("Enter a text \n")

if("make money online" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("suscribe now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("" in text):
    spam = True