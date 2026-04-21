# import tkinter
from tkinter import *
import pymysql
import tkinter.messagebox as m

#creating a Main window
r=Tk()
r.geometry("400x400")
r.title("My Title")
r.configure(bg="orange")


# Connection Function
def CreateConn():
    return pymysql.connect(host="localhost" , database="tkinter" , user ="root" , password="Sk7321807046", port=3306)


def InsertData():
    r =ern.get()
    f =efn.get()
    l =eln.get()
    e =eem.get()
    
    if(r==""or f=="" or l=="" or e==""):
        m.showinfo("Insert Status", "All fields are mandatory")
    
    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (r,f,l,e)
            query = "insert into student(rollno,fname,lname,email)values(%s,%s,%s,%s)"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("Insert Status", "Data Inserted")
            conn.close()
        except Exception as ee:
            print("Insert Exception:",ee)


#Adding labels in Main windows
rn = Label(r,text="Roll No")
rn.place(x=20,y=20)

fn = Label(r,text="First Name")
fn.place(x=20,y=60)

ln = Label(r,text="Last Name")
ln.place(x=20,y=100)

em = Label(r,text="Email")
em.place(x=20,y=140)

#Adding Entry box Into Main Window
ern = Entry()
ern.place(x=100 , y=20)

efn =Entry()
efn.place(x=100 , y=60)

eln =Entry()
eln.place(x=100 , y=100)

eem =Entry()
eem.place(x=100 , y=140)


#Adding Buttons into Main Window
button1 = Button(r, text ="Insert", bg="white" , command=InsertData )
button1.place(x=20 , y=200)


mainloop()