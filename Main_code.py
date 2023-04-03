import tkinter
from tkinter import *
from tkinter import messagebox
from hi import *
import random
z=tkinter.Tk()
z.geometry('1800x1200')
text = 'abcdefghijklmnopqrstuvwxyz0123456789'
k=random.choices(text, k=5)
r=''.join(k)
def cap():
    f=aa3.get()
    if r==f:
        mainf()
    else:
        messagebox.showinfo('Wrong','Wrong captcha')
def login():
    d=aa1.get()
    e=aa2.get()
    if d=='T' and e=='T':
        cap()
    else:
        messagebox.showinfo('Invaid','Incorrect Details')
ca=Canvas(z,width=1800,height=1200,bg='Orange')
ca.place(x=0,y=0)
ca.create_rectangle(100,100,1400,700,width=5,fill='white')
ca.create_line(630,210,840,210,width=5,fill='orange')
ca.create_rectangle(610,370,850,500,width=5,fill='orange')
a4=Label(z,text='LOGIN',fg='black',font=('Elephant',30),bg='white')
a4.place(x=650,y=150)
a1=Label(z,text='User ID',fg='black',font=('Elephant',15),bg='white')
a1.place(x=550,y=250)
aa1=Entry(z,width=30,bg='orange')
aa1.place(x=700,y=255)
a2=Label(z,text='Password',fg='black',font=('Elephant',15),bg='white')
a2.place(x=550,y=300)
aa2=Entry(z,width=30,show='*',bg='orange')
aa2.place(x=700,y=305)
a3=Label(z,text=r,width=10,font=('Elephant',12),fg='black',bg='white')
a3.place(x=665,y=400)
aa3=Entry(z,width=25,bg='white')
aa3.place(x=650,y=450)
a4=Button(z,text='Login',width=10,font=('Elephant',12),fg='black',command=login,bg='orange')
a4.place(x=660,y=530)
z.mainloop()