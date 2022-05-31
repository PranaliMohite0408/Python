from tkinter import *

frm_login = Tk()

frm_login.title("Login")

#frm_login.maxsize(width=1080, height=1920)

frm_login.minsize(width=1080, height=1920)

#Label


lbl_Login = Label(frm_login, text="Login", fg="Black", font=("Helvetica", 40))
lbl_Login.place(x=200,y=10)


lbl_Username = Label(frm_login, text="Username", bg="Orange", fg="white", font=("Helvetica", 30))
lbl_Username.place(x=40,y=120)

lbl_Password = Label(frm_login, text="Password", bg="Orange", fg="white", font=("Helvetica", 30))
lbl_Password.place(x=40,y=200)

#Entry
var = StringVar()
txt_Login = Entry(frm_login, bg="White", bd=5, textvariable=var, width=50, font=("Helvetica", 15))
txt_Login.place(x=260,y=120)


Password = StringVar()
txt_Login = Entry(frm_login, bg="White", bd=5, textvariable=Password, width=50, font=("Helvetica", 15))
txt_Login.place(x=260,y=200)

#Buttons
btn_Submit = Button(frm_login, text="Submit", bg="Black", fg="white", font=("Helvetica",30))
btn_Submit.place(x=250, y=300)

frm_login.mainloop()