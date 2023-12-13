# l1=["iam","you are"]
# l2=["healty","fine","ok"]
# # for x in l1:
# #     i=0
# #     while(i<len(l2)):
# #          print(x,l2[i])
# #          i+=1
# # print()
# n = 4
# for i in range(2,11):
#     for n in range(2,11           ):
#         print(i,"X",n,"=",n*i)
#     print()   
# l1=[1,2]
# l2=[4,5]
# for x in l1:
#     i=0
#     while(i<len(l2)):
#          print(x,l2[i])
#          i+=1
# print()
row = 5
s=row
# for i in range(row):
#      print()
#      for i in range(i+1):
#         print("*",end=" ")
# for i in range(row):
#      print()
#      for i in range(row-i):
#         print("*",end=" ") 
# for i in range(row):
#      print()
#      print(" "*s,end=" ")
#      for i in range(i+1):
#         print("*",end=" ")
#      s-=1
# s=1
# for i in range(row):
#      print()
#      print(" "*s,end=" ")
#      for i in range(row-i):
#         print("*",end=" ")
#      s+=1

# row = 5
# for i in range(row):
#     print()
#     for j in range(row):
#         if i == 0  or i == row-1 or j == 0 or  j==row-1 :
#             print("*",end=" ")
      
#         else:
#             print(" ",end=" ")

row = 4

for roww in range(row):
    print()
    for coloumn in range(row):
       if (roww == 0 or roww == row-1 or coloumn == 0 or coloumn == row-1):
         print("X",end=" ")
       else:
            print(" ",end=" ")