
with open('poem.txt','r') as f:
    a=f.read()
    if "twinkle" in a:
        print("Twinkle is present")
    else:
        print("Twinkle is not present.")

# print(a)
