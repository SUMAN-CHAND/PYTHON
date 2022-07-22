# Use open function to read the contant of a file !
f=open('sample.txt')  #by default the mode is r
# data=f.read() 
data=f.read(5) #read first 5 characters 
print(data)
f.close()