words=["donkey","mote","kadu"]


with open('sample2.txt','r') as f:
    content=f.read()
for word in words:
    content=content.replace(word,"$#%#%^!&")


with open('sample2.txt','w') as f:
    f.write(content)