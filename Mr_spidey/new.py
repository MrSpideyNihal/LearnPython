from tkinter import * 
import sys 
def getValue():
    a = uid.get()
    b = pass2.get()
    
if __name__ == "__main__":
    window = Tk()
    window.title("FORM")
    window.geometry('350x400')
    window.configure(bg="black")

    uid = StringVar()
    pass2 = StringVar()

    label = Label(window,text = "Username",bg="black",fg='white',font='Algerian')
    label1 = Label(window,text = "Password",bg="black",fg='white',font='Algerian')
    label2 = Label(window,text = "Gender",bg="black",fg='white',font='Algerian')
    label3 = Label(window,text = "HOBBIES",bg="black",fg='white',font='Algerian')
    label4 = Label(window,text = "Country",bg="black",fg='white',font='Algerian')


    btn = Button(window,bg="yellow",text='SUBMIT! ',width=15,height=1,font='Algerian',command=getValue)  
    rb1 = Radiobutton(window,text="MALE",bg="black",fg='white',font='Algerian',value=1)
    rb2 = Radiobutton(window,text="FEMALE",bg="black",fg='white',font='Algerian',value=2)
    cb  = Checkbutton(window,text="READING",bg="black",fg='white',font='Algerian')
    cb1 = Checkbutton(window,text="SIGNING",bg="black",fg='white',font='Algerian')
    cb2 = Checkbutton(window,text="RUNNING",bg="black",fg='white',font='Algerian')
    cb3 = Checkbutton(window,text="SWIMING",bg="black",fg='white',font='Algerian')


    e1=Entry(window,bg="white",fg='black',textvariable = uid)
    e2=Entry(window,bg="white",fg='black',textvariable = pass2,show="#" )

    #placeing
    
    rb1.place(x=130,y =100)
    rb2.place(x=210,y =100)
    btn.place(x=60,y=250)
    cb.place(x=120,y=150)
    cb1.place(x=220,y=150)
    cb2.place(x=120,y=170)
    cb3.place(x=220,y=170)



    label.place(x=20,y=10)
    label1.place(x=20,y=50)
    label2.place(x=20,y=100)
    label3.place(x=20,y=150)
    label4.place(x=20,y=200)

    e1.place(x=140,y=10 )
    e2.place(x=140,y=50)
   
    window.mainloop()