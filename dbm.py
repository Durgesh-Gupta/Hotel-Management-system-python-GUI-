import pymysql as p
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def getConnection():
    serverName='localhost'
    userName='root'
    passw=""
    dbName='durgesh'
    return p.connect(serverName,userName,passw,dbName)

def exit():
    root.quit()
def bookRegister():
    uname1=uname.get()
    people1=people.get()
    contact1=contact.get()
    roomtype1=roomtype.get()
    nday1=nday.get()
    
    global price,Totalbill
    price={'normal':2000,
    'delux':5000,
    'full delux':8000}

    if roomtype1.isnumeric():
        
        nprice={0:'normal',1:'delux',2:'full delux'}
        Totalbill=int(price[nprice[int(roomtype1)-1]])*int(nday1)
    else:
        Totalbill=price[roomtype1]*int(nday1)

    t=(uname1,people1,contact1,roomtype1,nday1,Totalbill)
    print(t)
    db=getConnection()
    sql="insert into user02(name,people,cont,roomtype,nday,bill) values(%s,%s,%s,%s,%s,%s);"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
    print("done")
    messagebox.showinfo("Check In", "Registration Completed...")

    exit()

    

    
def addBook(): 
    global uname,people,contact,roomtype,nday
    root = Tk()

    root.minsize(width=400,height=400)
    root.geometry("500x500")
    root.title("Check In Page")
    root.configure(background='#dbbeed')
    


    
    db=getConnection()
    cr=db.cursor()
    
    lb1 = Label(root,text="Name : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.20)
        
    uname = Entry(root)
    uname.place(relx=0.3,rely=0.20, relwidth=0.62)
        
    lb2 = Label(root,text="No. of People : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25)
        
    people = Entry(root)
    people.place(relx=0.3,rely=0.25, relwidth=0.62)
        
    lb3 = Label(root,text="Contact : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.30)
        
    contact = Entry(root)
    contact.place(relx=0.3,rely=0.30, relwidth=0.62)
        
    lb4 = Label(root,text="roomtype : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.35)
        
    roomtype = Entry(root)
    roomtype.place(relx=0.3,rely=0.35, relwidth=0.62)

    lb5 = Label(root,text="1.Normal 2.Delux 3.full Delux ", bg='black', fg='white')
    lb5.place(relx=0.3,rely=0.39, relheight=0.04)

    lb6 = Label(root,text="No. of Days : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.44, relheight=0.08)
        
    nday = Entry(root)
    nday.place(relx=0.3,rely=0.44, relwidth=0.62)
    
    submit = Button(root,text="SUBMIT",bg='#d1ccc0', fg='WHITE',command=bookRegister)
    submit.place(relx=0.3,rely=0.55, relwidth=0.18,relheight=0.08)
    
   
    root.mainloop()

# Guest List

def getList():
    root = Tk()
    root.geometry("600x250") 
    root.configure(background='#dbbeed')
    root.title("Guest List")

    db = getConnection()
    cr = db.cursor()
    cr.execute("SELECT * FROM user02")
    i=0 
    for user02 in cr: 
        for j in range(len(user02)):
            e = Entry(root, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, user02[j])
        i=i+1
    root.mainloop()

# Check Out

def Checkout():
    global lb2
    root = Tk()
    root.title("Check Out")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.configure(background='#dbbeed')


    lb1 = Label(root,text="Booking ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    lb2 = Entry(root)
    lb2.place(relx=0.2,rely=0.2, relheight=0.08)
    
    Bid = Button(root,text="CheckOut",bg='black', fg='white', command=getbill)
    Bid.place(relx=0.15,rely=0.3, relwidth=0.62, relheight=0.08)
    root.mainloop()
 
def Delete():
    id=lb2.get()
    db=getConnection()
    sql="delete from user02 where id=%s"
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()
    print("Delted")


def getbill():
    
    root = Tk()
    root.title("Bill")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.configure(background='#dbbeed')

    id3=lb2.get()
    
    db=getConnection()
    sql=("select bill from user02 where id=%s")
    cr=db.cursor()
    cr.execute(sql,id3)
    bill=cr.fetchall()
    
    

    lb1 = Label(root,text="Booking ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
    
    Bid = Label(root,text=id3, bg='black', fg='white')
    Bid.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    l2 = Label(root,text="Totall Bill : ", bg='black', fg='white')
    l2.place(relx=0.05,rely=0.35, relheight=0.08)

    uname = Label(root,text=bill, bg='black', fg='white')
    uname.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    Delete()
    root.mainloop()





    






