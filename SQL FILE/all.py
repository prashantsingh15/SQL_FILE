from tkinter import*

window=Tk()

window.title("Welcome to My web")


window.minsize(width=200,height=400)


window.maxsize(width=400,height=800)


l1=Label(window,text="Emp name",fg="blue",bg="brown")


l1.place(x=0,y=10)

v=StringVar()
def edtech():
    x=v.get()
    print(x)
    l2.config(text=x)

e1=Entry(window,font=("corbel",10),bd=5,textvariable=v)


e1.place(x=80,y=10)


b1=Button(window,text="Enter",fg="yellow",bg="green",command=edtech)


b1.place(x=100,y=60)


l2=Label(window,text=" ",fg="red",bg="brown")


l2.place(x=120,y=100)



window.mainloop()