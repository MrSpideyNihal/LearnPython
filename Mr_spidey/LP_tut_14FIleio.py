# File handling is an  imp part for any web application
# we can read and write  in a file
# we have : r mode,a mode ,w mode ,x mode 
'''
#steps :
         1.open a file
         2.read or write
         3.close the file 
'''

# functions : 1.read() 2.readline() 3.read(14)
#             4.write() 5.open()


# open
# myfile = open('sample.txt','w')
# myfile.write("HELLO WORLD")
# print(myfile.read)
# myfile.close
#write
# myfile = open('sample.txt','a')
# myfile.write("MR_SPIDEY ")
# print(myfile.read)
# myfile.close()                       
#create
# myfile1 = open('sample1.txt','x')
# print(myfile1)
# myfile1.
#read
# myfile = open('sample.txt','r')
# str=myfile.read()
# print(str)
# str1=myfile.read(5)
# print(str1)
# str2=myfile.readline()
# print(str2)
# str3=myfile.readline()
# print(str3)
# myfile.close()

#rename
# import os
# os.rename('sample1.txt','newfile.txt')
# os.remove('newfile.txt')
import os
fname = input("Enter your file name ! ")

run=True
while(run):
      print("\n\n\n")
      print("ENTER YOUR OPERATION WHICH YOU WANT TO DO !")
      print("Enter 1 for Read file \n Enter 2 for write content in file ")
      print("Enter 3 for remove file \n Enter 4 for Exit! ")
      ch = int(input("ENTER YOUR CHOICE ! : "))
      if(ch==1):
          myfile = open(fname,'r')
          str=myfile.read()
          print(str)
          myfile.close()  
      elif(ch==2):
          myfile = open(fname,'a')
          value = input("START WRITING : ")
          myfile.write(value)
          myfile.close()  
      elif(ch==3):
          os.remove(fname)
      elif(ch==4):
          print("EXIT!    ")
          run = False
      else:
        print("INVALID CHOICE")