file1='copy.txt'
file2='this.txt'

with open('copy.txt') as f:
    content1=f.read()

with open('this.txt') as f:
    content2=f.read()

if content1==content2:
    print("Two file has same content")
else:
    print("Two file has not same content")