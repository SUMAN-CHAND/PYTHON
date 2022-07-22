import os

oldfile="sample3.txt"

with open(oldfile) as f:
    content=f.read()

with open('renamed_by_python.txt', 'w') as f:
    f.write(content)

os.remove(oldfile)
