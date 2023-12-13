# Functons --> it is a block of code which can be written
# once and can be excecuted whenever required in program.

# advantages :
#             1. it prevents more space  to full fill
#             2.it prevents rewriting the code
#             3.code can be reused later.

# It is define by "def" keyword.


# syntax of function : 
#                     def functionname() :
                        # statement

# # example : 
# def greet():
#     print("Good Morning !")

# greet() #functions needs to be called after declaration.

# #Types of function : 
#   there are 4 types of function : 
#        1.function with no argument and no return value 
#        2.function with  argument and no return value 
#        3.function with no argument and  return value 
#        4.function with  argument and  return value 

#   1.function with no argument and no return value 

#   example:

# def sqr():
#     num = 6
#     sqrt1= num**2
#     print("Square of ",num," is : " , sqrt1)

# # now we had to call it
# sqr()


#   2.function with  argument and no return value :
#   example :

# def sqr(num):
#     sqrt = num **2
#     print("Square of ",num," is : ", sqrt)

#     # now call it 
# sqr(5)

# 3.function with no argument and  return value 

#  example:
# num = 6
# def sqr():
   
#     sqrt1 = 6 ** 2
#     # print("The square of ",num," is : ",sqrt)
#     return sqrt1
# obj = sqr()
# print("SUBSCRIBE TO COOL PIKACHU ! ><")
# print("SQUARE OF ",num," = ", obj)



# 4.function with  argument and  return value 

# example:

# def sqr(num):
#     sqrt1=num**2
#     return sqrt1
# obj= sqr(5)
# print("subscribe to COOL PIKACHU!")
# print("Square of 5 is : ",obj)



# def sum(num1,num2):
#     print("The addtion of numbers is ",num1+num2)
# def sub():
#     num1=6
#     num2=5
#     print("The subtraction of numbers is ",num1-num2)
 
# def mul():
#     num1=6
#     num2=5
#     return num1*num2


# def div(num1,num2):
    
#     return num1/num2


# sum(1,4)
# sub()
# obj1=mul()
# print(obj1)
# obj2=div(2,4)
# print(obj2)


# def evenn(num1):
#     if(num1%2==0):
#         print("num is even")
#     else:
#         print("ODD NUMBER")


# evenn(12)
# def fact(value):
#        i = 1
#        fact = 1
#        while(i<=value):
#            fact = fact * i
#            i+=1
#        print("Facrtorial is ", fact)

# fact(3)

# def FindPercentage(sub1,sub2,sub3,sub4):
#     total = sub1+sub2+sub3+sub4
#     percentage = total/400 * 100
#     print("The percentage is : ",percentage)
# FindPercentage(99,89,99,99)

def CALCULATE(n1,n2):
    print("Enter your choice !")
    print(" 'a' for add \n 'b' for sub \n 'c' for multiplication   ")
    value = input(" 'd' for divide   ")
    if   value == 'a':
        print("The addtion of ",n1," and ",n2," is : ",n1+n2)
    elif value == 'b':
        print("The Subtraction of ",n1," and ",n2," is : ",n1-n2)
    elif value == 'c':
        print("The Multiplication of ",n1," and ",n2," is : ",n1*n2)
    elif value == 'd':
        print("The Division of ",n1," and ",n2," is : ",n1/n2) 
    else:
        print("INVALID INPUT!")
CALCULATE(6,5)