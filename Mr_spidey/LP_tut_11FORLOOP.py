# name = " hello "
# for x in name:
#     print(x,end="")
# mylist =  []
# for i in range(1,11):
#     mylist.append(i)
# print(mylist)
# mylist = [25,30,35,40,45,50,55]
# ecount= 0
# ocount = 0
# sum = 0
# sub = 1
# for i in range(len(mylist)):
#     if(mylist[i]%2==0):
#         print("Even number foune ",mylist[i])
#         ecount=ecount+1
#         sum =  mylist[i]+sum
#     else:
#         print("Odd number found" ,mylist[i])
#         ocount=ocount+1
#         sub =  mylist[i]*sub

# print("even number  : ",ecount )
# print("odd  number  : ",ocount )
# print("The addtion of even number is : ",sum)
# print("The product of odd num is : ",sub)



#CONTINUE-:
#BREAK----: break is  a keyword w
#PASS-----:
str = "hellonerf"
# for i in str:
#     if i == 'n':
#          break
#     print(i)\
# i = 1
# while i<=10 : 
#    if i==5:
#        break
#    print(i)
#    i+=1
i = 0
while i<=10 : 
   i+=1
   if i==5:
       continue
   print(i,end="\t")
