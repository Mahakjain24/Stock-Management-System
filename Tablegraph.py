import tkinter
from tkinter import *
import pymysql
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def table1():
    t=tkinter.Tk()
    t.geometry('1600x1100')
    ca=Canvas(t,width=1800,height=1200,bg='Orange')
    ca.create_line(600,50,600,700,width=3)
    ca.place(x=0,y=0)
    def t1():
        c=Canvas(t,width=850,height=600,bg='white')
        c.place(x=650,y=60)
        x=pymysql.connect(host='localhost',user='root',password='root',database='stockmarket')
        y=x.cursor()
        sql="select Item_Name,Price_per_piece from item"
        inn=[]
        ppp=[]
        y.execute(sql)
        data1=y.fetchall()
        for j in data1:
            inn.append(j[0])
            ppp.append(j[1])
        i=np.arange(len(inn))
        fig=plt.figure(figsize=(23,10),dpi=40)
        plt.bar(i,ppp,color='r',label='Items')
        plt.title('Items and price chart',fontsize=25)
        plt.xlabel('Items',fontsize=20)
        plt.ylabel('Price per piece',fontsize=20)
        plt.xticks(i,inn,rotation=15,fontsize=15)
        plt.legend(loc=0)
        ch=FigureCanvasTkAgg(fig,c)
        ch.get_tk_widget().place(x=0,y=0)
        plt.show()
    def t2():
        c=Canvas(t,width=850,height=600,bg='white')
        c.place(x=650,y=60)
        x=pymysql.connect(host='localhost',user='root',password='root',database='stockmarket')
        y=x.cursor()
        sql="select Item_Name,Open_Qty,Current_Qty from item"
        inn=[]
        oq=[]
        cq=[]
        y.execute(sql)
        data2=y.fetchall()
        for j in data2:
            inn.append(j[0])
            oq.append(j[1])
            cq.append(j[2])
        i=np.arange(len(inn))
        fig=plt.figure(figsize=(23,10),dpi=40)
        width=0.3
        plt.bar(i,oq,width,color='g',label='Open Quantity')
        plt.bar(i+width,cq,width,color='y',label='Current Quantity')
        plt.title('Items and Quantities',fontsize=25)
        plt.xlabel('Items',fontsize=20)
        plt.ylabel('Open and Current Qty',fontsize=20)
        plt.xticks(i+width/2,inn,rotation=15,fontsize=15)
        plt.legend(loc=0)
        ch=FigureCanvasTkAgg(fig,c)
        ch.get_tk_widget().place(x=0,y=0)
        plt.show()
    def t3():
        c=Canvas(t,width=850,height=600,bg='white')
        c.place(x=650,y=60)
        x=pymysql.connect(host='localhost',user='root',password='root',database='stockmarket')
        y=x.cursor()
        sql="select StockID,Quantity from stockin"
        s=[]
        q=[]
        y.execute(sql)
        data1=y.fetchall()
        for j in data1:
            s.append(j[0])
            q.append(j[1])
        i=np.arange(len(s))
        fig=plt.figure(figsize=(23,10),dpi=40)
        plt.bar(i,q,color='g',label='Quantity')
        plt.title('StockID and Quantity',fontsize=25)
        plt.xlabel('Stock ID',fontsize=20)
        plt.ylabel('Quantity',fontsize=20)
        plt.xticks(i,s,rotation=15,fontsize=15)
        plt.legend(loc=0)
        ch=FigureCanvasTkAgg(fig,c)
        ch.get_tk_widget().place(x=0,y=0)
        plt.show()
    a=Label(t,text='Items Vs Price Per Piece',fg='black',font=('Elephant',15),bg='orange')
    a.place(x=160,y=300)
    a1=Button(t,text='Graph 1',fg='black',font=('Elephant',12),bg='orange',width=10,command=t1)
    a1.place(x=450,y=295)
    b=Label(t,text='Items Vs Open and Current Quantity',fg='black',font=('Elephant',15),bg='orange')
    b.place(x=50,y=350)
    b1=Button(t,text='Graph 2',fg='black',font=('Elephant',12),bg='orange',width=10,command=t2)
    b1.place(x=450,y=345)
    c=Label(t,text='Stock ID Vs Quantity',fg='black',font=('Elephant',15),bg='orange')
    c.place(x=190,y=400)
    c1=Button(t,text='Graph 3',fg='black',font=('Elephant',12),bg='orange',width=10,command=t3)
    c1.place(x=450,y=395)
    t.mainloop()   