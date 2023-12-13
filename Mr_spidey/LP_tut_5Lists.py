# list meth0.ods

#list is a collection of element.
#eg mylist = [1,2,3,4,5,6,7,8,9]

'''
features : 
           1.list elments are in order
           2.list are mutable(can add delete update element)
           3.duplicate value are allowed
           4.multiple data types can be 
'''
#index      0 1 2 3 4    5     6 7   8 
new_list = [1,2,3,4,5,"hello ",7,8,True]
#-index    -9-8-7-6-5   -4    -3-2  -1
# print ("Element in list",new_list)
# print ("Value of list at index 4 is ",new_list[4])
# print(new_list[-7:-1])
# new_list.append("mango")#ADDING ELEMENT IN LAST
# new_list.insert(3,"kivi")
# new_list.extend([11,12,13])
# print(new_list)
# new_list.reverse()
# print(new_list)
# print("Length of string",len(new_list))
# a=new_list[::-1]
# print(a)
# mylist = [1,2,3,4,5,6,7,8,9,2]
# print(sorted(mylist,reverse = True))
# print(mylist.index(2))
# print(mylist.count(2))
# mylist.pop()
# print(mylist)
# # mylist.clear()

# print(mylist+mylist)
# print(mylist*2000000)

# mylist = [2,[3,4],5,4,6]
# print(mylist[1][0])

# list1 = []
# list1.append(1)
# list1.extend([2,3,4,5,6,7])
# print(list1)

mylist = [1,2,3,4,5,6,7,8]
print("The Addtion of list is :",sum(mylist))
print("The maximum num in list is",max(mylist))
print("The minimum num in list is",min(mylist))
print(mylist[1:-2:2])
mylist1 = mylist.copy()
print(mylist1)
print(mylist[:5])
print(mylist[1:])