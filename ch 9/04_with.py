with open('anyother.txt','r') as f:
    a=f.read()

with open('anyother.txt','w') as f:
    a=f.write("I am writing")
    
print(a)
