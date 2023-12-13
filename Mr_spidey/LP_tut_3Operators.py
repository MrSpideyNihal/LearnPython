'''helloo this is multi line comment '''
#hello this is single line comment 
# NOTE FOR USING COMMENT YOU MUST USE # OR ''' ''' 
#Output is here ------------------->

'''
add = a+b
sub = a-b
mul = a*b
div = a/b
remainder = a%b
'''
'''
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))

OPERATORS 
1.Arn ope
print ("The addtion of a and b is ",a,"+",b,"=",a+b)
print ("The subtraction of a and b is ",a,"-",b,"=",a-b) 
print ("The Multiplication of a and b is ",a,"*",b,"=",a*b) 
print ("The Square of a is ",a,"** 2","=",a**2) 
print ("The float division of a and b is ",a,"/",b,"=",a/b) 
print ("The division of a and b is ",a,"//",b,"=",a//b) 
print ("The remainder of a and b is ",a,"%",b,"=",a%b)

'''

# getnum = int(input("Enter a num : "))
# if (getnum%2==0):
# 	print("given num is a EVEN no")
# else :
# 	print("given number is ODD NUM")


# 2.COMPARE OPERATORS
# THESE ARE COMPARE OPERATOR '<','>','<=','>=','==','!='
# a = 50
# b = 30
# print("a<b",a<b)
# print("a>b",a>b)
# print("a<=b",a<=b)
# print("a>=b",a>=b)
# print("a!=b",a!=b)
# print("a==b",a==b)

# a = int(input("Enter a value"))
# b = int(input("Enter b value"))

# print("a<b",a<b)
# print("a>b",a>b)
# print("a<=b",a<=b)
# print("a>=b",a>=b)
# print("a!=b",a!=b)
# print("a==b",a==b)

#logical Operator
#and(),or(),not()
'''
a=True
b=False
print("a and b output : ",a and b)
print("a or b output : ",a or b)
print("a not b output : ",not a,not b)

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




3. Identity Operator :     it is used to compare the objects  if both the 
                           objects are actually of the same data type and
                           share the same memory location. 

                1. is  , 2nd is not

# 1. is
a = 5
b = 5
c = 6
print(a is b) #checks Memory location
#2. is not
print(a is not c) # also checks Memory location


Assignment Operator
=,-=,+=,*=,/=,//=,%=

b=30
A=50
print("value ",A)
A+=b
print("after add ",A)
A-=b
print("after sub ",A)
A*=b
print("After multiply ",A)
A/=b
print("After float dividing",A)
A//=b
print("After dividing ",A)
A%=b
print("After doing modulos ",A)

Membership Operator : it test for membership in a sequence such as Strings,Lists or table


   in  , not in

6.Bitwise Operator
'''
''' bitwise AND '&'
    bitwise OR '!'
   bitwise XOR '^'
  bitwise NOT '~'
  bitwise LEFT SHIFT <<
  bitwise RIGHT SHIFT >>'''
a = 10
b = 12
print("A = ",a," b = ",b)
c = b&a #both bit are 1 so output will 1
print("AND OPERATOR :",c)
c = b|a  #any bit are 1 so output will 1
print(" OR OPERATOR :",c)
c = b^a  #both are  0 so op is 0 
print(" XOR OPERATOR :",c)
a = ~a  #Reverse the bit 1's complement
print(" (NOT) Inverted :",a)
a = 10
c = a<<2  #Left Shift shift n num bit to left
print(" Left shifted valued :",c)
c = a>>1#Right Shift shift n num bit to left
print("Right shifted valued :",c)
