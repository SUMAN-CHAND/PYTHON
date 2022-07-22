def parsentage(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p



marks1=[63,68,85,77]
# parsentage1=((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100
parsentage1=parsentage(marks1)
marks2=[66,89,75,87]
# parsentage2=((marks2[0]+marks2[1]+marks2[2]+marks2[3])/400)*100
parsentage2=parsentage(marks2)

print(parsentage1,parsentage2)