from ast import operator
from fileinput import close


# f=open('anyother.txt','w')
f=open('anyother.txt','a')
f.write("I am appending")
f,close()