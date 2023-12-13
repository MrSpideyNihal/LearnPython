from tkinter import *
#-----------------------functions----------------------#
global t1,t2,t3,t4,t5,t6,t7 

def putdata():
    myfile = open("newfile.pdf",'a')
    myfile.write(t1.get())

    myfile.write("<center><b><u>{Department}</u></b></center>")
    myfile.write(t2.get())

    myfile.close() 



#----------------main loop-----------------------------------------------#
if __name__ == "__main__":
    window = Tk()
    window.title("FORM")
    window.geometry('800x400')
    window.configure(bg="Black")
#-------------------------Labels-------------------------------------------#

    label = Label(window,text = "College Name",bg="black",fg='white',font='Algerian')
    label1 = Label(window,text = "Department",bg="black",fg='white',font='Algerian')
    label2 = Label(window,text = "Test Type",bg="black",fg='white',font='Algerian')
    label3 = Label(window,text = "Subject",bg="black",fg='white',font='Algerian')
    label4 = Label(window,text = "Time",bg="black",fg='white',font='Algerian')
    label5 = Label(window,text = "Marks",bg="black",fg='white',font='Algerian')
    label6 = Label(window,text = "Date",bg="black",fg='white',font='Algerian')

#-------------------------Entry--------------------------------------------#

    t1 =Entry(window,fg="black",bg='white')
    t2 =Entry(window,fg="black",bg='white')
    t3 =Entry(window,fg="black",bg='white')
    t4 =Entry(window,fg="black",bg='white')
    t5 =Entry(window,fg="black",bg='white')
    t6 =Entry(window,fg="black",bg='white')
    t7 =Entry(window,fg="black",bg='white')


#--------------------------Button------------------------------------------#

    Submit = Button(window,text = "SUBMIT",bg="Yellow",fg='Red',font='Algerian',width=15,height=2,command=putdata)
    
 
#---------------------------placeing section-------------------------------#

    label.place(x=20,y=20)
    label1.place(x=400,y=20)
    label2.place(x=20,y=120)
    label3.place(x=400,y=120)
    label4.place(x=20,y=220)
    label5.place(x=400,y=220)
    label6.place(x=20,y=320)

    t1.place(x=180,y=20)
    t2.place(x=540,y=20)
    t3.place(x=180,y=120)
    t4.place(x=540,y=120)
    t5.place(x=180,y=220)
    t6.place(x=540,y=220)
    t7.place(x=180,y=320)

    Submit.place(x=405,y=300)


    window.mainloop()