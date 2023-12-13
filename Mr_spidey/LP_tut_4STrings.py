#string methods
name = "MR SPIDEY"
print("The string is  : ",name)
print("Length of the name is: ",len(name))
print("Upper case ",name.upper())
print("Lower case ",name.lower())                   
print("The position of character P in string ",name," is ",name.find('P'))
print("The character in position 3 in string ",name," is ",name[3])
print("Positive Slicing name by index 1 and 5 :",name[1:7])
print("Negative Slicing name by index 1 and 5 :",name[-7:-4])
print(name.replace("MR SPIDEY","DEKU"))
firstname="NARUTO"
lastname="{} UZUMAKI"

print(firstname + lastname)
print(lastname.format(firstname))