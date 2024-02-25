from tkinter import*
window=Tk()
i1=PhotoImage(file="C:/Users/bunty/OneDrive/Desktop/6-5anna merie.png")

l1=Label(window,text="I am Prashant",bg="blue",fg="red",width=40)
l1.pack()
l1.grid(row=0,column=1)
l1.place(x=15,y=10)
window.title("Welcome to My world")
window.minsize(width=100,height=200)
window.maxsize(width=300,height=800)
window.mainloop()
