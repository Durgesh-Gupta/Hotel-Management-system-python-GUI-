from tkinter import *
from PIL import ImageTk,Image
from dbm import *


root = Tk()
root.title("Hotel Management System")
root.minsize(width=400,height=400)
root.geometry("800x500")

background =Image.open("hotel.jpg")

background = background.resize((1000,816),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background)
Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = 1000, height = 816)
Canvas1.pack(expand=True,fill=BOTH)

frame = Frame(root)
frame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
heading = Label(frame, text="Hotel Management System", bg='black' ,fg='#f7bb16'
, font=('Times New Roman',20,'bold'))
heading.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Booking",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Check Out",bg='black', fg='white', command=Checkout)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Guest List",bg='black', fg='white', command=getList)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Exit",bg='black', fg='white', command = exit)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

def exit():
    root.quit()
root.mainloop()
