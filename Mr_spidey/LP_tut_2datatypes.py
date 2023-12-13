#variables 
a = 1
b = 2
c = "MR_Spidey"
A = True
# 2a = 5  not valid 
print(a)
print(A)
print(b)
print(type(c))

name = "MR_SPIDEY"
age = 17 
address = "Manish nagar"

print(name)
print(age)
print(address)

x=y=z=50
print(x,y,z)

m,n,o=6,4,3
print(m,n,o)

print(list(range(0, 11)))
print(len(name))

add = a+b
sub = a-b
mul = a*b
div = a/b
remainder = a%b

print("a<b",a<b)
print("a>b",a>b)
print("a<=b",a<=b)
print("a>=b",a>=b)
print("a!=b",a!=b)
print("a==b",a==b)

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

if(a>b) and (a>c) :
	print(a," is the greatest number")
elif(b>a) and (b>c) :
	print(b," is the greatest number")
elif(c>a) and (c>b):
	print(c," is the greatest number")
else:
	print("all number are equal")