def remove_word(string,word):
    new_string=string.replace(word,"")
    return new_string.strip()


this="      Suman is a coder        "

s=remove_word(this,"Suman")
print(s)

# print(this)
# print(this.strip())